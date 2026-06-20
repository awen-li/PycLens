# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_truncate_after_read_or_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.BytesIO(b'A' * 10)
    bufio = self.tp(raw, 100)
    self.assertEqual(bufio.read(2), b'AA')
    self.assertEqual(bufio.truncate(), 2)
    self.assertEqual(bufio.write(b'BB'), 2)
    self.assertEqual(bufio.truncate(), 4)
