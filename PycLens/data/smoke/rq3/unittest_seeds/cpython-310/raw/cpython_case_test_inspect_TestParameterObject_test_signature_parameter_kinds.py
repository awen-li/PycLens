# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestParameterObject_test_signature_parameter_kinds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = inspect.Parameter
    self.assertTrue(P.POSITIONAL_ONLY < P.POSITIONAL_OR_KEYWORD < P.VAR_POSITIONAL < P.KEYWORD_ONLY < P.VAR_KEYWORD)
    self.assertEqual(str(P.POSITIONAL_ONLY), 'POSITIONAL_ONLY')
    self.assertTrue('POSITIONAL_ONLY' in repr(P.POSITIONAL_ONLY))
