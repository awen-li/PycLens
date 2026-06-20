# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_write_error_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO()

    def bad_write(b):
        raise OSError()
    raw.write = bad_write
    b = self.tp(raw)
    b.write(b'spam')
    self.assertRaises(OSError, b.close)
    self.assertTrue(b.closed)
