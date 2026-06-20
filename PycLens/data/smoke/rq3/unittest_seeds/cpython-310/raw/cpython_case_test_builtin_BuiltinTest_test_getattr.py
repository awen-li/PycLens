# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_getattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(getattr(sys, 'stdout') is sys.stdout)
    self.assertRaises(TypeError, getattr, sys, 1)
    self.assertRaises(TypeError, getattr, sys, 1, 'foo')
    self.assertRaises(TypeError, getattr)
    self.assertRaises(AttributeError, getattr, sys, chr(sys.maxunicode))
    self.assertRaises(AttributeError, getattr, 1, '\udad1픞')
