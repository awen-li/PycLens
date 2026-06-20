# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_read_and_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO((b'asdf', b'ghjk'))
    rw = self.tp(raw, 8)
    self.assertEqual(b'as', rw.read(2))
    rw.write(b'ddd')
    rw.write(b'eee')
    self.assertFalse(raw._write_stack)
    self.assertEqual(b'ghjk', rw.read())
    self.assertEqual(b'dddeee', raw._write_stack[0])
