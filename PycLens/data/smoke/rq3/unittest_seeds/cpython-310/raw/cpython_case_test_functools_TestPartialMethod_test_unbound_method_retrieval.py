# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialMethod_test_unbound_method_retrieval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj = self.A
    self.assertFalse(hasattr(obj.both, '__self__'))
    self.assertFalse(hasattr(obj.nested, '__self__'))
    self.assertFalse(hasattr(obj.over_partial, '__self__'))
    self.assertFalse(hasattr(obj.static, '__self__'))
    self.assertFalse(hasattr(self.a.static, '__self__'))
