# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __new__(cls, a=1, *args, **kwargs):
            return object.__new__(cls)

    class B(A):

        def __init__(self, b):
            pass

    class C(A):

        def __new__(cls, a=1, b=2, *args, **kwargs):
            return object.__new__(cls)

    class D(A):
        pass
    self.assertEqual(self.signature(B), ((('b', ..., ..., 'positional_or_keyword'),), ...))
    self.assertEqual(self.signature(C), ((('a', 1, ..., 'positional_or_keyword'), ('b', 2, ..., 'positional_or_keyword'), ('args', ..., ..., 'var_positional'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(D), ((('a', 1, ..., 'positional_or_keyword'), ('args', ..., ..., 'var_positional'), ('kwargs', ..., ..., 'var_keyword')), ...))
