# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestParameterObject_test_signature_parameter_immutability

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = inspect.Parameter('spam', kind=inspect.Parameter.KEYWORD_ONLY)
    with self.assertRaises(AttributeError):
        p.foo = 'bar'
    with self.assertRaises(AttributeError):
        p.kind = 123
