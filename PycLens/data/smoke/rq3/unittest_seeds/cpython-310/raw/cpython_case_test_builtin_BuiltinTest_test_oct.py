# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_oct

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(oct(100), '0o144')
    self.assertEqual(oct(-100), '-0o144')
    self.assertRaises(TypeError, oct, ())
