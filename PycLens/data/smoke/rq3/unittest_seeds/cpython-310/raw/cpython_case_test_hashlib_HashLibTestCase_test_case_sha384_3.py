# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_case_sha384_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('sha384', b'a' * 1000000, '9d0e1809716474cb086e834e310a4a1ced149e9c00f248527972cec5704c2a5b' + '07b8b3dc38ecc4ebae97ddd87f3d8985')
