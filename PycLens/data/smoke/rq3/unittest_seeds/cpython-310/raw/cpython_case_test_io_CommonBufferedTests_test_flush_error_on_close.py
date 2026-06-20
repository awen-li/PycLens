# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_flush_error_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO()
    closed = []

    def bad_flush():
        closed[:] = [b.closed, raw.closed]
        raise OSError()
    raw.flush = bad_flush
    b = self.tp(raw)
    self.assertRaises(OSError, b.close)
    self.assertTrue(b.closed)
    self.assertTrue(raw.closed)
    self.assertTrue(closed)
    self.assertFalse(closed[0])
    self.assertFalse(closed[1])
    raw.flush = lambda : None
