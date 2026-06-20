# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestIntermixedArgs_test_exclusive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PROG')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--foo', action='store_true', help='FOO')
    group.add_argument('--spam', help='SPAM')
    parser.add_argument('badger', nargs='*', default='X', help='BADGER')
    args = parser.parse_intermixed_args('1 --foo 2'.split())
    self.assertEqual(NS(badger=['1', '2'], foo=True, spam=None), args)
    self.assertRaises(ArgumentParserError, parser.parse_intermixed_args, '1 2'.split())
    self.assertEqual(group.required, True)
