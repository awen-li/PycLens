# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_compattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        class computed_attribute(object):

            def __init__(self, get, set=None, delete=None):
                self.__get = get
                self.__set = set
                self.__delete = delete

            def __get__(self, obj, type=None):
                return self.__get(obj)

            def __set__(self, obj, value):
                return self.__set(obj, value)

            def __delete__(self, obj):
                return self.__delete(obj)

        def __init__(self):
            self.__x = 0

        def __get_x(self):
            x = self.__x
            self.__x = x + 1
            return x

        def __set_x(self, x):
            self.__x = x

        def __delete_x(self):
            del self.__x
        x = computed_attribute(__get_x, __set_x, __delete_x)
    a = C()
    self.assertEqual(a.x, 0)
    self.assertEqual(a.x, 1)
    a.x = 10
    self.assertEqual(a.x, 10)
    self.assertEqual(a.x, 11)
    del a.x
    self.assertNotHasAttr(a, 'x')
