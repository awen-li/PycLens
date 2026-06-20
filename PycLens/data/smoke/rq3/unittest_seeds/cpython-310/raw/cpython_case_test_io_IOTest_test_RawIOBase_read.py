# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_RawIOBase_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIOWithoutRead((b'abc', b'd', None, b'efg', None))
    self.assertEqual(rawio.read(2), b'ab')
    self.assertEqual(rawio.read(2), b'c')
    self.assertEqual(rawio.read(2), b'd')
    self.assertEqual(rawio.read(2), None)
    self.assertEqual(rawio.read(2), b'ef')
    self.assertEqual(rawio.read(2), b'g')
    self.assertEqual(rawio.read(2), None)
    self.assertEqual(rawio.read(2), b'')
