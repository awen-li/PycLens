# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_seek_and_tell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.BytesIO(b'asdfghjkl')
    rw = self.tp(raw)
    self.assertEqual(b'as', rw.read(2))
    self.assertEqual(2, rw.tell())
    rw.seek(0, 0)
    self.assertEqual(b'asdf', rw.read(4))
    rw.write(b'123f')
    rw.seek(0, 0)
    self.assertEqual(b'asdf123fl', rw.read())
    self.assertEqual(9, rw.tell())
    rw.seek(-4, 2)
    self.assertEqual(5, rw.tell())
    rw.seek(2, 1)
    self.assertEqual(7, rw.tell())
    self.assertEqual(b'fl', rw.read(11))
    rw.flush()
    self.assertEqual(b'asdf123fl', raw.getvalue())
    self.assertRaises(TypeError, rw.seek, 0.0)
