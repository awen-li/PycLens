# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syslog.py
# case: Test_test_setlogmask

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mask = syslog.LOG_UPTO(syslog.LOG_WARNING)
    oldmask = syslog.setlogmask(mask)
    self.assertEqual(syslog.setlogmask(0), mask)
    self.assertEqual(syslog.setlogmask(oldmask), mask)
