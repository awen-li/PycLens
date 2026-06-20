# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_classmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Test:

        @classmethod
        def foo(cls, arg1, *, arg2=1):
            pass
    meth = Test().foo
    self.assertEqual(self.signature(meth), ((('arg1', ..., ..., 'positional_or_keyword'), ('arg2', 1, ..., 'keyword_only')), ...))
    meth = Test.foo
    self.assertEqual(self.signature(meth), ((('arg1', ..., ..., 'positional_or_keyword'), ('arg2', 1, ..., 'keyword_only')), ...))
