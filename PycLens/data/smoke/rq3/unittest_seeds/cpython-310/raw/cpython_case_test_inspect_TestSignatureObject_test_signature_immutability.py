# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_immutability

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(a):
        pass
    sig = inspect.signature(test)
    with self.assertRaises(AttributeError):
        sig.foo = 'bar'
    with self.assertRaises(TypeError):
        sig.parameters['a'] = None
