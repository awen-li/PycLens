# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in range(-30, 30):
        self.assertEqual(hash(x), hash(complex(x, 0)))
        x /= 3.0
        self.assertEqual(hash(x), hash(complex(x, 0.0)))
