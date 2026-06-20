# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_annotations_with_local_namespaces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:
        ...

    def func(foo: Foo) -> int:
        pass

    def func2(foo: Foo, bar: 'Bar') -> int:
        pass
    for signature_func in (inspect.signature, inspect.Signature.from_callable):
        with self.subTest(signature_func=signature_func):
            sig1 = signature_func(func)
            self.assertEqual(sig1.return_annotation, int)
            self.assertEqual(sig1.parameters['foo'].annotation, Foo)
            sig2 = signature_func(func, locals=locals())
            self.assertEqual(sig2.return_annotation, int)
            self.assertEqual(sig2.parameters['foo'].annotation, Foo)
            sig3 = signature_func(func2, globals={'Bar': int}, locals=locals())
            self.assertEqual(sig3.return_annotation, int)
            self.assertEqual(sig3.parameters['foo'].annotation, Foo)
            self.assertEqual(sig3.parameters['bar'].annotation, 'Bar')
