# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_all_new_methods_are_called

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):
        pass

    class B(object):
        counter = 0

        def __new__(cls):
            B.counter += 1
            return super().__new__(cls)

    class C(A, B):
        pass
    self.assertEqual(B.counter, 0)
    C()
    self.assertEqual(B.counter, 1)
