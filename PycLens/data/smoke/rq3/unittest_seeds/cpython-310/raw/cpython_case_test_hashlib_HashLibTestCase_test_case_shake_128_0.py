# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_case_shake_128_0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('shake_128', b'', '7f9c2ba4e88f827d616045507605853ed73b8093f6efbc88eb1a6eacfa66ef26', True)
    self.check('shake_128', b'', '7f9c', True)
