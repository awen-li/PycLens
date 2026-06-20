# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_get_paths

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    scheme = get_paths()
    default_scheme = get_default_scheme()
    wanted = _expand_vars(default_scheme, None)
    wanted = sorted(wanted.items())
    scheme = sorted(scheme.items())
    self.assertEqual(scheme, wanted)
