# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_ipow_returns_not_implemented

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __ipow__(self, other):
            return NotImplemented

    class B(A):

        def __rpow__(self, other):
            return 1

    class C(A):

        def __pow__(self, other):
            return 2
    a = A()
    b = B()
    c = C()
    a **= b
    self.assertEqual(a, 1)
    c **= b
    self.assertEqual(c, 2)
