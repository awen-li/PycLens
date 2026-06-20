# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_registration_builtins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):
        pass
    A.register(int)
    self.assertIsInstance(42, A)
    self.assertIsInstance(42, (A,))
    self.assertTrue(issubclass(int, A))
    self.assertTrue(issubclass(int, (A,)))

    class B(A):
        pass
    B.register(str)

    class C(str):
        pass
    self.assertIsInstance('', A)
    self.assertIsInstance('', (A,))
    self.assertTrue(issubclass(str, A))
    self.assertTrue(issubclass(str, (A,)))
    self.assertTrue(issubclass(C, A))
    self.assertTrue(issubclass(C, (A,)))
