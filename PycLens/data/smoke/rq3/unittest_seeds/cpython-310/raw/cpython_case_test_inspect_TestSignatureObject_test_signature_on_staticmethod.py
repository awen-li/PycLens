# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_staticmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Test:

        @staticmethod
        def foo(cls, *, arg):
            pass
    meth = Test().foo
    self.assertEqual(self.signature(meth), ((('cls', ..., ..., 'positional_or_keyword'), ('arg', ..., ..., 'keyword_only')), ...))
    meth = Test.foo
    self.assertEqual(self.signature(meth), ((('cls', ..., ..., 'positional_or_keyword'), ('arg', ..., ..., 'keyword_only')), ...))
