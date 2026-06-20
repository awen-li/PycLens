# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_netrc.py
# case: NetrcTestCase_test_file_not_found_in_home

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_cwd(None) as d:
        with os_helper.EnvironmentVarGuard() as environ:
            environ.set('HOME', d)
            self.assertRaises(FileNotFoundError, netrc.netrc)
