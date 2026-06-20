# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_setattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    setattr(sys, 'spam', 1)
    self.assertEqual(sys.spam, 1)
    self.assertRaises(TypeError, setattr, sys, 1, 'spam')
    self.assertRaises(TypeError, setattr)
