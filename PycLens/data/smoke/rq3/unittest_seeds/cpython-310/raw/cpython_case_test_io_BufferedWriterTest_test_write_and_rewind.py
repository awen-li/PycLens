# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_write_and_rewind

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = io.BytesIO()
    bufio = self.tp(raw, 4)
    self.assertEqual(bufio.write(b'abcdef'), 6)
    self.assertEqual(bufio.tell(), 6)
    bufio.seek(0, 0)
    self.assertEqual(bufio.write(b'XY'), 2)
    bufio.seek(6, 0)
    self.assertEqual(raw.getvalue(), b'XYcdef')
    self.assertEqual(bufio.write(b'123456'), 6)
    bufio.flush()
    self.assertEqual(raw.getvalue(), b'XYcdef123456')
