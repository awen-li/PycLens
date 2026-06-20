# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binop.py
# case: FallbackBlockingTests_test_fallback_ne_blocking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (e, sn, xn) = (SupEq(), SN(), XN())
    self.assertFalse(e != e)
    self.assertRaises(TypeError, ne, e, sn)
    self.assertRaises(TypeError, ne, sn, e)
    self.assertFalse(e != xn)
    self.assertRaises(TypeError, ne, xn, e)
