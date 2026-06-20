# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_srcdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    srcdir = sysconfig.get_config_var('srcdir')
    self.assertTrue(os.path.isabs(srcdir), srcdir)
    self.assertTrue(os.path.isdir(srcdir), srcdir)
    if sysconfig._PYTHON_BUILD:
        Python_h = os.path.join(srcdir, 'Include', 'Python.h')
        self.assertTrue(os.path.exists(Python_h), Python_h)
        self.assertTrue(sysconfig._is_python_source_dir(srcdir))
    elif os.name == 'posix':
        makefile_dir = os.path.dirname(sysconfig.get_makefile_filename())
        makefile_dir = os.path.realpath(makefile_dir)
        self.assertEqual(makefile_dir, srcdir)
