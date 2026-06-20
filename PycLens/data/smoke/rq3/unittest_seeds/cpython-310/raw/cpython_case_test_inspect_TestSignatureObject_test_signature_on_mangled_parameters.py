# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_mangled_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Spam:

        def foo(self, __p1: 1=2, *, __p2: 2=3):
            pass

    class Ham(Spam):
        pass
    self.assertEqual(self.signature(Spam.foo), ((('self', ..., ..., 'positional_or_keyword'), ('_Spam__p1', 2, 1, 'positional_or_keyword'), ('_Spam__p2', 3, 2, 'keyword_only')), ...))
    self.assertEqual(self.signature(Spam.foo), self.signature(Ham.foo))
