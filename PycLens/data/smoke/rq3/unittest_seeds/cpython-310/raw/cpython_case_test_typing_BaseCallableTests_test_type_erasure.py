# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_type_erasure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable

    class C1(Callable):

        def __call__(self):
            return None
    a = C1[[int], T]
    self.assertIs(a().__class__, C1)
    self.assertEqual(a().__orig_class__, C1[[int], T])
