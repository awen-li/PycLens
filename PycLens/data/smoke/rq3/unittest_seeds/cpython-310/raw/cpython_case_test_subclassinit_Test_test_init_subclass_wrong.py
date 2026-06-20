# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_init_subclass_wrong

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __init_subclass__(cls, whatever):
            pass
    with self.assertRaises(TypeError):

        class B(A):
            pass
