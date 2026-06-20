# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_registration_transitiveness

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):
        pass
    self.assertTrue(issubclass(A, A))
    self.assertTrue(issubclass(A, (A,)))

    class B(metaclass=abc_ABCMeta):
        pass
    self.assertFalse(issubclass(A, B))
    self.assertFalse(issubclass(A, (B,)))
    self.assertFalse(issubclass(B, A))
    self.assertFalse(issubclass(B, (A,)))

    class C(metaclass=abc_ABCMeta):
        pass
    A.register(B)

    class B1(B):
        pass
    self.assertTrue(issubclass(B1, A))
    self.assertTrue(issubclass(B1, (A,)))

    class C1(C):
        pass
    B1.register(C1)
    self.assertFalse(issubclass(C, B))
    self.assertFalse(issubclass(C, (B,)))
    self.assertFalse(issubclass(C, B1))
    self.assertFalse(issubclass(C, (B1,)))
    self.assertTrue(issubclass(C1, A))
    self.assertTrue(issubclass(C1, (A,)))
    self.assertTrue(issubclass(C1, B))
    self.assertTrue(issubclass(C1, (B,)))
    self.assertTrue(issubclass(C1, B1))
    self.assertTrue(issubclass(C1, (B1,)))
    C1.register(int)

    class MyInt(int):
        pass
    self.assertTrue(issubclass(MyInt, A))
    self.assertTrue(issubclass(MyInt, (A,)))
    self.assertIsInstance(42, A)
    self.assertIsInstance(42, (A,))
