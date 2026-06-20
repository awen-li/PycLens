# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_from_callable_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MySignature(inspect.Signature):
        pass

    class foo:
        pass
    foo_sig = MySignature.from_callable(foo)
    self.assertIsInstance(foo_sig, MySignature)
