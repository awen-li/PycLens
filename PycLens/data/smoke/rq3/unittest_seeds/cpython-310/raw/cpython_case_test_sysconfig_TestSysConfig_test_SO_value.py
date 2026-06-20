# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_SO_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with check_warnings(('', DeprecationWarning)):
        self.assertEqual(sysconfig.get_config_var('SO'), sysconfig.get_config_var('EXT_SUFFIX'))
