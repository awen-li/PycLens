# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binop.py
# case: FallbackBlockingTests_test_fallback_rmethod_blocking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (e, f, s, x) = (SupEq(), F(), S(), X())
    self.assertEqual(e, e)
    self.assertEqual(e, f)
    self.assertEqual(f, e)
    self.assertEqual(e, x)
    self.assertRaises(TypeError, eq, x, e)
    self.assertRaises(TypeError, eq, e, s)
    self.assertRaises(TypeError, eq, s, e)
