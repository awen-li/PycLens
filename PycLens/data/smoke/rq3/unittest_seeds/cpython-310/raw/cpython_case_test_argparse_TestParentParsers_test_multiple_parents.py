# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_multiple_parents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parents = [self.abcd_parent, self.wxyz_parent]
    parser = ErrorRaisingArgumentParser(parents=parents)
    self.assertEqual(parser.parse_args('--d 1 --w 2 3 4'.split()), NS(a='3', b=None, d='1', w='2', y=None, z='4'))
