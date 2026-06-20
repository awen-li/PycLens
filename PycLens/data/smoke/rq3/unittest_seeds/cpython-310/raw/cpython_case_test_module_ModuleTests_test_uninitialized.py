# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_uninitialized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    foo = ModuleType.__new__(ModuleType)
    self.assertTrue(foo.__dict__ is None)
    self.assertRaises(TypeError, dir, foo)
    try:
        s = foo.__name__
        self.fail('__name__ = %s' % repr(s))
    except AttributeError:
        pass
    self.assertEqual(foo.__doc__, ModuleType.__doc__)
