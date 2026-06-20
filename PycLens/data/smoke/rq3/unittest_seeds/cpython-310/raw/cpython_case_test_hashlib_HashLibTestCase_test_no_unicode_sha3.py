# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_no_unicode_sha3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_no_unicode('sha3_224')
    self.check_no_unicode('sha3_256')
    self.check_no_unicode('sha3_384')
    self.check_no_unicode('sha3_512')
    self.check_no_unicode('shake_128')
    self.check_no_unicode('shake_256')
