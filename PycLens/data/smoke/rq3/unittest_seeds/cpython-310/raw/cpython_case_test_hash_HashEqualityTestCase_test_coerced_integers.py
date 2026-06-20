# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashEqualityTestCase_test_coerced_integers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.same_hash(int(1), int(1), float(1), complex(1), int('1'), float('1.0'))
    self.same_hash(int(-2 ** 31), float(-2 ** 31))
    self.same_hash(int(1 - 2 ** 31), float(1 - 2 ** 31))
    self.same_hash(int(2 ** 31 - 1), float(2 ** 31 - 1))
    self.same_hash(int(2 ** 31), float(2 ** 31))
    self.same_hash(int(-2 ** 63), float(-2 ** 63))
    self.same_hash(int(2 ** 63), float(2 ** 63))
