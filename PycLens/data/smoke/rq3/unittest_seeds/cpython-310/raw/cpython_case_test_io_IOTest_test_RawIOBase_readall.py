# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_RawIOBase_readall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIOWithoutRead((b'abc', b'd', b'efg'))
    self.assertEqual(rawio.read(), b'abcdefg')
    rawio = self.MockRawIOWithoutRead((b'abc', b'd', b'efg'))
    self.assertEqual(rawio.readall(), b'abcdefg')
