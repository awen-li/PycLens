# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: InfNanTest_test_inf_signs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(copysign(1.0, float('inf')), 1.0)
    self.assertEqual(copysign(1.0, float('-inf')), -1.0)
