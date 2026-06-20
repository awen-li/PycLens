# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_EXT_SUFFIX_in_vars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _imp
    vars = sysconfig.get_config_vars()
    self.assertIsNotNone(vars['SO'])
    self.assertEqual(vars['SO'], vars['EXT_SUFFIX'])
    self.assertEqual(vars['EXT_SUFFIX'], _imp.extension_suffixes()[0])
