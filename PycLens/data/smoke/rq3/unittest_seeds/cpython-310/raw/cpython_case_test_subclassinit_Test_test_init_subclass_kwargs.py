# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_init_subclass_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __init_subclass__(cls, **kwargs):
            cls.kwargs = kwargs

    class B(A, x=3):
        pass
    self.assertEqual(B.kwargs, dict(x=3))
