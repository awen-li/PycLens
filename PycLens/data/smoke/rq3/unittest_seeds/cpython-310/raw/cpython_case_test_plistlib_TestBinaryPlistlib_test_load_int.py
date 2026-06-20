# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestBinaryPlistlib_test_load_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.decode(b'\x10\x00'), 0)
    self.assertEqual(self.decode(b'\x10\xfe'), 254)
    self.assertEqual(self.decode(b'\x11\xfe\xdc'), 65244)
    self.assertEqual(self.decode(b'\x12\xfe\xdc\xba\x98'), 4275878552)
    self.assertEqual(self.decode(b'\x13\x01#Eg\x89\xab\xcd\xef'), 81985529216486895)
    self.assertEqual(self.decode(b'\x13\xfe\xdc\xba\x98vT2\x10'), -81985529216486896)
