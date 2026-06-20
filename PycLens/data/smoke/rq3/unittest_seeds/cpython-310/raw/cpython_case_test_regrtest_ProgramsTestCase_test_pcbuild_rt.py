# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ProgramsTestCase_test_pcbuild_rt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = os.path.join(ROOT_DIR, 'PCbuild\\rt.bat')
    if not os.path.isfile(script):
        self.skipTest(f'File "{script}" does not exist')
    rt_args = ['-q']
    if platform.machine() == 'ARM64':
        rt_args.append('-arm64')
    elif platform.machine() == 'ARM':
        rt_args.append('-arm32')
    elif platform.architecture()[0] == '64bit':
        rt_args.append('-x64')
    if Py_DEBUG:
        rt_args.append('-d')
    self.run_batch(script, *rt_args, *self.regrtest_args, *self.tests)
