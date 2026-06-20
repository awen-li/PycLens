# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_same_argument_name_parents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parents = [self.wxyz_parent, self.z_parent]
    parser = ErrorRaisingArgumentParser(parents=parents)
    self.assertEqual(parser.parse_args('1 2'.split()), NS(w=None, y=None, z='2'))
