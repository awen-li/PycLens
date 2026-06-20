# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_flush_and_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.BytesIO(b'abcdefghi')
    bufio = self.tp(raw)
    bufio.write(b'123')
    bufio.flush()
    bufio.write(b'45')
    bufio.flush()
    bufio.seek(0, 0)
    self.assertEqual(b'12345fghi', raw.getvalue())
    self.assertEqual(b'12345fghi', bufio.read())
