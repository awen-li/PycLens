# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_builtins_test_unbound_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    signature = inspect.signature(o)
    self.assertTrue(isinstance(signature, inspect.Signature))
    self.assertEqual(list(signature.parameters.values())[0].name, 'self')
    return signature
