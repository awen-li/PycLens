# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: DecryptionTests_test_good_password

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.zip.setpassword(b'python')
    self.assertEqual(self.zip.read('test.txt'), self.plain)
    self.zip2.setpassword(b'12345')
    self.assertEqual(self.zip2.read('zero'), self.plain2)
