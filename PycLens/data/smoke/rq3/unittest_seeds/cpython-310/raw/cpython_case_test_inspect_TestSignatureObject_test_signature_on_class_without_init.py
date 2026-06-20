# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_class_without_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass
    self.assertEqual(str(inspect.signature(C)), '()')

    class D(C):
        pass
    self.assertEqual(str(inspect.signature(D)), '()')

    class C(type):
        pass

    class D(C):
        pass
    with self.assertRaisesRegex(ValueError, 'callable.*is not supported'):
        self.assertEqual(inspect.signature(C), None)
    with self.assertRaisesRegex(ValueError, 'callable.*is not supported'):
        self.assertEqual(inspect.signature(D), None)
