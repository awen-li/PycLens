# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_subparser_parents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    subparsers = parser.add_subparsers()
    abcde_parser = subparsers.add_parser('bar', parents=[self.abcd_parent])
    abcde_parser.add_argument('e')
    self.assertEqual(parser.parse_args('bar -b 1 --d 2 3 4'.split()), NS(a='3', b='1', d='2', e='4'))
