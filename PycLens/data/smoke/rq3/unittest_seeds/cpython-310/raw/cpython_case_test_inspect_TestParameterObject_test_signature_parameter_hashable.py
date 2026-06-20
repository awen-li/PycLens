# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestParameterObject_test_signature_parameter_hashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = inspect.Parameter
    foo = P('foo', kind=P.POSITIONAL_ONLY)
    self.assertEqual(hash(foo), hash(P('foo', kind=P.POSITIONAL_ONLY)))
    self.assertNotEqual(hash(foo), hash(P('foo', kind=P.POSITIONAL_ONLY, default=42)))
    self.assertNotEqual(hash(foo), hash(foo.replace(kind=P.VAR_POSITIONAL)))
