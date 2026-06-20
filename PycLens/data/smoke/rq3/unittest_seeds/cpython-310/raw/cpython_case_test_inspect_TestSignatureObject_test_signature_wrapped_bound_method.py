# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_wrapped_bound_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Test:

        def m1(self, arg1, arg2=1) -> int:
            pass

    @functools.wraps(Test().m1)
    def m1d(*args, **kwargs):
        pass
    self.assertEqual(self.signature(m1d), ((('arg1', ..., ..., 'positional_or_keyword'), ('arg2', 1, ..., 'positional_or_keyword')), int))
