# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_uninitialized_modules

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from types import ModuleType as M
    m = M.__new__(M)
    str(m)
    self.assertNotHasAttr(m, '__name__')
    self.assertNotHasAttr(m, '__file__')
    self.assertNotHasAttr(m, 'foo')
    self.assertFalse(m.__dict__)
    m.foo = 1
    self.assertEqual(m.__dict__, {'foo': 1})
