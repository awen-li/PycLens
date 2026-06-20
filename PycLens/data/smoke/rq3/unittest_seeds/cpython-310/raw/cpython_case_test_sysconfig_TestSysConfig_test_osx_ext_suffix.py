# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_osx_ext_suffix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    suffix = sysconfig.get_config_var('EXT_SUFFIX')
    self.assertTrue(suffix.endswith('-darwin.so'), suffix)
