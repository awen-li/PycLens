# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: DecryptionTests_test_bad_password

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.zip.setpassword(b'perl')
    self.assertRaises(RuntimeError, self.zip.read, 'test.txt')
    self.zip2.setpassword(b'perl')
    self.assertRaises(RuntimeError, self.zip2.read, 'zero')
