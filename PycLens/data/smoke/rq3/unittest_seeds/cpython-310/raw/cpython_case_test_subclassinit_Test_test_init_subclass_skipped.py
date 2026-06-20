# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_init_subclass_skipped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BaseWithInit:

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.initialized = cls

    class BaseWithoutInit(BaseWithInit):
        pass

    class A(BaseWithoutInit):
        pass
    self.assertIs(A.initialized, A)
    self.assertIs(BaseWithoutInit.initialized, BaseWithoutInit)
