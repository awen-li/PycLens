# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_blocksize_name_sha3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_blocksize_name('sha3_224', 144, 28)
    self.check_blocksize_name('sha3_256', 136, 32)
    self.check_blocksize_name('sha3_384', 104, 48)
    self.check_blocksize_name('sha3_512', 72, 64)
    self.check_blocksize_name('shake_128', 168, 0, 32)
    self.check_blocksize_name('shake_256', 136, 0, 64)
