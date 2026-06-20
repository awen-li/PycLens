# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_boolcontext

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(100):
        self.assertTrue(complex(random() + 1e-06, random() + 1e-06))
    self.assertTrue(not complex(0.0, 0.0))
