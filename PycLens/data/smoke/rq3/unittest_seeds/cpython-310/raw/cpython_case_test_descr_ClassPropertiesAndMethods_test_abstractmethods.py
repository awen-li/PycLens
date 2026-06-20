# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_abstractmethods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(AttributeError, getattr, type, '__abstractmethods__')

    class meta(type):
        pass
    self.assertRaises(AttributeError, getattr, meta, '__abstractmethods__')

    class X(object):
        pass
    with self.assertRaises(AttributeError):
        del X.__abstractmethods__
