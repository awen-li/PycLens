# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: RotatingFileHandlerTest_test_file_created

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rh = logging.handlers.RotatingFileHandler(self.fn, encoding='utf-8')
    rh.emit(self.next_rec())
    self.assertLogFile(self.fn)
    rh.close()
