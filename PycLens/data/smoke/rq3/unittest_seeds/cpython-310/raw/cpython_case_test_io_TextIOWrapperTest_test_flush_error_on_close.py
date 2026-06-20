# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_flush_error_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = self.TextIOWrapper(self.BytesIO(self.testdata), encoding='ascii')
    closed = []

    def bad_flush():
        closed[:] = [txt.closed, txt.buffer.closed]
        raise OSError()
    txt.flush = bad_flush
    self.assertRaises(OSError, txt.close)
    self.assertTrue(txt.closed)
    self.assertTrue(txt.buffer.closed)
    self.assertTrue(closed)
    self.assertFalse(closed[0])
    self.assertFalse(closed[1])
    txt.flush = lambda : None
