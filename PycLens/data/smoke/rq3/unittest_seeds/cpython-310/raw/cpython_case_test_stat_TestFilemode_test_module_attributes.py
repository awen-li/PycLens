# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_stat.py
# case: TestFilemode_test_module_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (key, value) in self.stat_struct.items():
        modvalue = getattr(self.statmod, key)
        self.assertEqual(value, modvalue, key)
    for (key, value) in self.permission_bits.items():
        modvalue = getattr(self.statmod, key)
        self.assertEqual(value, modvalue, key)
    for key in self.file_flags:
        modvalue = getattr(self.statmod, key)
        self.assertIsInstance(modvalue, int)
    for key in self.formats:
        modvalue = getattr(self.statmod, key)
        self.assertIsInstance(modvalue, int)
    for key in self.format_funcs:
        func = getattr(self.statmod, key)
        self.assertTrue(callable(func))
        self.assertEqual(func(0), 0)
