# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestBinaryPlistlib_test_load_singletons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(self.decode(b'\x00'), None)
    self.assertIs(self.decode(b'\x08'), False)
    self.assertIs(self.decode(b'\t'), True)
    self.assertEqual(self.decode(b'\x0f'), b'')
