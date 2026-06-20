# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_extra_sha3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_sha3('sha3_224', 448, 1152, b'\x06')
    self.check_sha3('sha3_256', 512, 1088, b'\x06')
    self.check_sha3('sha3_384', 768, 832, b'\x06')
    self.check_sha3('sha3_512', 1024, 576, b'\x06')
    self.check_sha3('shake_128', 256, 1344, b'\x1f')
    self.check_sha3('shake_256', 512, 1088, b'\x1f')
