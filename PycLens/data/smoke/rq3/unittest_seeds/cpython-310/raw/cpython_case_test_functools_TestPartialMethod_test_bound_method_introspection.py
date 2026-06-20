# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialMethod_test_bound_method_introspection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj = self.a
    self.assertIs(obj.both.__self__, obj)
    self.assertIs(obj.nested.__self__, obj)
    self.assertIs(obj.over_partial.__self__, obj)
    self.assertIs(obj.cls.__self__, self.A)
    self.assertIs(self.A.cls.__self__, self.A)
