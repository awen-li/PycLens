# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_vars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(set(vars()), set(dir()))
    self.assertEqual(set(vars(sys)), set(dir(sys)))
    self.assertEqual(self.get_vars_f0(), {})
    self.assertEqual(self.get_vars_f2(), {'a': 1, 'b': 2})
    self.assertRaises(TypeError, vars, 42, 42)
    self.assertRaises(TypeError, vars, 42)
    self.assertEqual(vars(self.C_get_vars()), {'a': 2})
