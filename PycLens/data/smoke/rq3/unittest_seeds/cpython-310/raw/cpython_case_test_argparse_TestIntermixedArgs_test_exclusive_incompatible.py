# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestIntermixedArgs_test_exclusive_incompatible

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PROG')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--foo', action='store_true', help='FOO')
    group.add_argument('--spam', help='SPAM')
    group.add_argument('badger', nargs='*', default='X', help='BADGER')
    self.assertRaises(TypeError, parser.parse_intermixed_args, [])
    self.assertEqual(group.required, True)
