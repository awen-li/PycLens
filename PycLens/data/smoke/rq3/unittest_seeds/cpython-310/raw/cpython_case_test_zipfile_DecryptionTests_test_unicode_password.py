# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: DecryptionTests_test_unicode_password

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.zip.setpassword, 'unicode')
    self.assertRaises(TypeError, self.zip.read, 'test.txt', 'python')
    self.assertRaises(TypeError, self.zip.open, 'test.txt', pwd='python')
    self.assertRaises(TypeError, self.zip.extract, 'test.txt', pwd='python')
