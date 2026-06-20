# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: FileHandlerTest_test_delay

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.unlink(self.fn)
    fh = logging.FileHandler(self.fn, encoding='utf-8', delay=True)
    self.assertIsNone(fh.stream)
    self.assertFalse(os.path.exists(self.fn))
    fh.handle(logging.makeLogRecord({}))
    self.assertIsNotNone(fh.stream)
    self.assertTrue(os.path.exists(self.fn))
    fh.close()
