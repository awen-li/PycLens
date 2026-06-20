# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestParameterObject_test_signature_parameter_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = inspect.Parameter
    p = P('foo', default=42, kind=inspect.Parameter.KEYWORD_ONLY)
    self.assertTrue(p == p)
    self.assertFalse(p != p)
    self.assertFalse(p == 42)
    self.assertTrue(p != 42)
    self.assertTrue(p == ALWAYS_EQ)
    self.assertFalse(p != ALWAYS_EQ)
    self.assertTrue(p == P('foo', default=42, kind=inspect.Parameter.KEYWORD_ONLY))
    self.assertFalse(p != P('foo', default=42, kind=inspect.Parameter.KEYWORD_ONLY))
