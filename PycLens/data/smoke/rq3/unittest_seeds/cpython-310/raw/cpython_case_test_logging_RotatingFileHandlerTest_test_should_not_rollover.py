# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: RotatingFileHandlerTest_test_should_not_rollover

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rh = logging.handlers.RotatingFileHandler(self.fn, encoding='utf-8', maxBytes=0)
    self.assertFalse(rh.shouldRollover(None))
    rh.close()
    rh = logging.handlers.RotatingFileHandler(os.devnull, encoding='utf-8', maxBytes=1)
    self.assertFalse(rh.shouldRollover(self.next_rec()))
    rh.close()
