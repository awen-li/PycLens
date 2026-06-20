# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_blocksize_name_blake2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_blocksize_name('blake2b', 128, 64)
    self.check_blocksize_name('blake2s', 64, 32)
