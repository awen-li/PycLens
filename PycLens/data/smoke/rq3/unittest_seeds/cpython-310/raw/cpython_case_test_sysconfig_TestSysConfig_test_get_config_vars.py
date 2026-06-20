# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_get_config_vars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cvars = get_config_vars()
    self.assertIsInstance(cvars, dict)
    self.assertTrue(cvars)
