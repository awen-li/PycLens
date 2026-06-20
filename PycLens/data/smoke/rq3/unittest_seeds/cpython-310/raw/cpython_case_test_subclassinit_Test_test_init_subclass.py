# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_init_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        initialized = False

        def __init_subclass__(cls):
            super().__init_subclass__()
            cls.initialized = True

    class B(A):
        pass
    self.assertFalse(A.initialized)
    self.assertTrue(B.initialized)
