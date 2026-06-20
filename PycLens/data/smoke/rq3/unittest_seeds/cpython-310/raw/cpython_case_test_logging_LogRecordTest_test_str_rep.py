# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LogRecordTest_test_str_rep

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = logging.makeLogRecord({})
    s = str(r)
    self.assertTrue(s.startswith('<LogRecord: '))
    self.assertTrue(s.endswith('>'))
