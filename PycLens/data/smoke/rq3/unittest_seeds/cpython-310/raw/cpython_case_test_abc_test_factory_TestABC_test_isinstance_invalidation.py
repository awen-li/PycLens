# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_isinstance_invalidation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):
        pass

    class B:
        pass
    b = B()
    self.assertFalse(isinstance(b, A))
    self.assertFalse(isinstance(b, (A,)))
    token_old = abc_get_cache_token()
    A.register(B)
    token_new = abc_get_cache_token()
    self.assertGreater(token_new, token_old)
    self.assertTrue(isinstance(b, A))
    self.assertTrue(isinstance(b, (A,)))
