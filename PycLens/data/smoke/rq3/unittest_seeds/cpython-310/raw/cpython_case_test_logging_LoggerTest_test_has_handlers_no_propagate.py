# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_has_handlers_no_propagate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    child_logger = logging.getLogger('blah.child')
    child_logger.propagate = False
    self.assertFalse(child_logger.hasHandlers())
