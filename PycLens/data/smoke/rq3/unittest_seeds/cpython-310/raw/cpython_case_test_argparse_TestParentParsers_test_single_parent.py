# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_single_parent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(parents=[self.wxyz_parent])
    self.assertEqual(parser.parse_args('-y 1 2 --w 3'.split()), NS(w='3', y='1', z='2'))
