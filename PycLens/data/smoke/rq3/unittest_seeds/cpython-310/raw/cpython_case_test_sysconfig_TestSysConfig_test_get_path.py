# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_get_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config_vars = get_config_vars()
    for scheme in _INSTALL_SCHEMES:
        for name in _INSTALL_SCHEMES[scheme]:
            expected = _INSTALL_SCHEMES[scheme][name].format(**config_vars)
            self.assertEqual(os.path.normpath(get_path(name, scheme)), os.path.normpath(expected))
