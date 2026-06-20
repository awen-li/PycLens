# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_srcdir_independent_of_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    srcdir = sysconfig.get_config_var('srcdir')
    with change_cwd(os.pardir):
        srcdir2 = sysconfig.get_config_var('srcdir')
    self.assertEqual(srcdir, srcdir2)
