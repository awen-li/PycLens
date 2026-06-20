# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestExitOnError_test_exit_on_error_with_good_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = self.parser.parse_args('--integers 4'.split())
    self.assertEqual(ns, argparse.Namespace(integers=4))
