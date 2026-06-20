# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_insane_timestamps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for func in (time.ctime, time.gmtime, time.localtime):
        for unreasonable in (-1e+200, 1e+200):
            self.assertRaises(OverflowError, func, unreasonable)
