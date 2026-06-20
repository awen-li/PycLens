# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_sys_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(sys.flags)
    attrs = ('debug', 'inspect', 'interactive', 'optimize', 'dont_write_bytecode', 'no_user_site', 'no_site', 'ignore_environment', 'verbose', 'bytes_warning', 'quiet', 'hash_randomization', 'isolated', 'dev_mode', 'utf8_mode', 'warn_default_encoding', 'int_max_str_digits')
    for attr in attrs:
        self.assertTrue(hasattr(sys.flags, attr), attr)
        attr_type = bool if attr == 'dev_mode' else int
        self.assertEqual(type(getattr(sys.flags, attr)), attr_type, attr)
    self.assertTrue(repr(sys.flags))
    self.assertEqual(len(sys.flags), len(attrs))
    self.assertIn(sys.flags.utf8_mode, {0, 1, 2})
