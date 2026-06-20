# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_struct_sizes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(zipfile.sizeEndCentDir, 22)
    self.assertEqual(zipfile.sizeCentralDir, 46)
    self.assertEqual(zipfile.sizeEndCentDir64, 56)
    self.assertEqual(zipfile.sizeEndCentDir64Locator, 20)
