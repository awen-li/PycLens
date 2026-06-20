# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_valid_context_extra

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DefaultContext = C.DefaultContext
    c = DefaultContext.copy()
    self.assertEqual(c._allcr, 1)
    c._allcr = 0
    self.assertEqual(c._allcr, 0)
