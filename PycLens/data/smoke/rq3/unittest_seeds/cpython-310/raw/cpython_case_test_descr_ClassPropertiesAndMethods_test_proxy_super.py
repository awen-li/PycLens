# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_proxy_super

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Proxy(object):

        def __init__(self, obj):
            self.__obj = obj

        def __getattribute__(self, name):
            if name.startswith('_Proxy__'):
                return object.__getattribute__(self, name)
            else:
                return getattr(self.__obj, name)

    class B(object):

        def f(self):
            return 'B.f'

    class C(B):

        def f(self):
            return super(C, self).f() + '->C.f'
    obj = C()
    p = Proxy(obj)
    self.assertEqual(C.__dict__['f'](p), 'B.f->C.f')
