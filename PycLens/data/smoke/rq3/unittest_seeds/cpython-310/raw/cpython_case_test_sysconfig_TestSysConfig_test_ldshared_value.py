# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_ldshared_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ldflags = sysconfig.get_config_var('LDFLAGS')
    ldshared = sysconfig.get_config_var('LDSHARED')
    self.assertIn(ldflags, ldshared)
