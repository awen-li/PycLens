# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_annotations_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        attr: int

    class B(A):
        pass

    class C(A):
        attr: str

    class D:
        attr2: int

    class E(A, D):
        pass

    class F(C, A):
        pass
    self.assertEqual(A.__annotations__, {'attr': int})
    self.assertEqual(B.__annotations__, {})
    self.assertEqual(C.__annotations__, {'attr': str})
    self.assertEqual(D.__annotations__, {'attr2': int})
    self.assertEqual(E.__annotations__, {})
    self.assertEqual(F.__annotations__, {})
