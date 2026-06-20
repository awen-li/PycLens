# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_registration_edge_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):
        pass
    A.register(A)

    class A1(A):
        pass
    self.assertRaises(RuntimeError, A1.register, A)

    class B(object):
        pass
    A1.register(B)
    A1.register(B)

    class C(A):
        pass
    A.register(C)
    self.assertRaises(RuntimeError, C.register, A)
    C.register(B)
