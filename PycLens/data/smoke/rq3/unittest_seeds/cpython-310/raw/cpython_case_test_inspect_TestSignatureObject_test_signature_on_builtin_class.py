# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_builtin_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = '(file, protocol=None, fix_imports=True, buffer_callback=None)'
    self.assertEqual(str(inspect.signature(_pickle.Pickler)), expected)

    class P(_pickle.Pickler):
        pass

    class EmptyTrait:
        pass

    class P2(EmptyTrait, P):
        pass
    self.assertEqual(str(inspect.signature(P)), expected)
    self.assertEqual(str(inspect.signature(P2)), expected)

    class P3(P2):

        def __init__(self, spam):
            pass
    self.assertEqual(str(inspect.signature(P3)), '(spam)')

    class MetaP(type):

        def __call__(cls, foo, bar):
            pass

    class P4(P2, metaclass=MetaP):
        pass
    self.assertEqual(str(inspect.signature(P4)), '(foo, bar)')
