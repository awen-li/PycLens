# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_blocksize_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_blocksize_name('md5', 64, 16)
    self.check_blocksize_name('sha1', 64, 20)
    self.check_blocksize_name('sha224', 64, 28)
    self.check_blocksize_name('sha256', 64, 32)
    self.check_blocksize_name('sha384', 128, 48)
    self.check_blocksize_name('sha512', 128, 64)
