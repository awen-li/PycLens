# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: StatisticsErrorTest_test_has_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    errmsg = 'Expected StatisticsError to be a ValueError, but got a subclass of %r instead.'
    self.assertTrue(hasattr(statistics, 'StatisticsError'))
    self.assertTrue(issubclass(statistics.StatisticsError, ValueError), errmsg % statistics.StatisticsError.__base__)
