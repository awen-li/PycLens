# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_copy_setstate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import copy

    class C(object):

        def __init__(self, foo=None):
            self.foo = foo
            self.__foo = foo

        def setfoo(self, foo=None):
            self.foo = foo

        def getfoo(self):
            return self.__foo

        def __getstate__(self):
            return [self.foo]

        def __setstate__(self_, lst):
            self.assertEqual(len(lst), 1)
            self_.__foo = self_.foo = lst[0]
    a = C(42)
    a.setfoo(24)
    self.assertEqual(a.foo, 24)
    self.assertEqual(a.getfoo(), 42)
    b = copy.copy(a)
    self.assertEqual(b.foo, 24)
    self.assertEqual(b.getfoo(), 24)
    b = copy.deepcopy(a)
    self.assertEqual(b.foo, 24)
    self.assertEqual(b.getfoo(), 24)
