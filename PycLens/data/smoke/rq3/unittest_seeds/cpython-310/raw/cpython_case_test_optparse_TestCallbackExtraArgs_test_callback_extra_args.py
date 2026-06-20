# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestCallbackExtraArgs_test_callback_extra_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-p1,2,3', '--point', '4,5,6'], {'points': [(1, 2, 3), (4, 5, 6)]}, [])
