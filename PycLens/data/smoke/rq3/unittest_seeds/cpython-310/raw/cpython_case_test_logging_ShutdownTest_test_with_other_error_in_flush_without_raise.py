# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ShutdownTest_test_with_other_error_in_flush_without_raise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    logging.raiseExceptions = False
    self._test_with_failure_in_method('flush', IndexError)
