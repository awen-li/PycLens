# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_is_integer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(1.1.is_integer())
    self.assertTrue(1.0.is_integer())
    self.assertFalse(float('nan').is_integer())
    self.assertFalse(float('inf').is_integer())
