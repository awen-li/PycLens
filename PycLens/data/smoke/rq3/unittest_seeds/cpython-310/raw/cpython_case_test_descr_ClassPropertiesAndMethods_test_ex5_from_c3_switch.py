# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_ex5_from_c3_switch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):
        pass

    class B(object):
        pass

    class C(object):
        pass

    class X(A):
        pass

    class Y(A):
        pass

    class Z(X, B, Y, C):
        pass
    self.assertEqual(Z.__mro__, (Z, X, B, Y, A, C, object))
