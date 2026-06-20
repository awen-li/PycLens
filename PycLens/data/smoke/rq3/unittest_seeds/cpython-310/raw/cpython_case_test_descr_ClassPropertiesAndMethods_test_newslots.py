# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_newslots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(list):

        def __new__(cls):
            self = list.__new__(cls)
            self.foo = 1
            return self

        def __init__(self):
            self.foo = self.foo + 2
    a = C()
    self.assertEqual(a.foo, 3)
    self.assertEqual(a.__class__, C)

    class D(C):
        pass
    b = D()
    self.assertEqual(b.foo, 3)
    self.assertEqual(b.__class__, D)
