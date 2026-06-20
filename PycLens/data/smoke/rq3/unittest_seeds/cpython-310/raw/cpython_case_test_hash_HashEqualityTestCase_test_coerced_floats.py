# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashEqualityTestCase_test_coerced_floats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.same_hash(int(1.23e+300), float(1.23e+300))
    self.same_hash(float(0.5), complex(0.5, 0.0))
