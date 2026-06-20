# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ProgramsTestCase_test_tools_buildbot_test

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = os.path.join(ROOT_DIR, 'Tools', 'buildbot', 'test.bat')
    test_args = ['--testdir=%s' % self.tmptestdir]
    if platform.machine() == 'ARM64':
        test_args.append('-arm64')
    elif platform.machine() == 'ARM':
        test_args.append('-arm32')
    elif platform.architecture()[0] == '64bit':
        test_args.append('-x64')
    if not Py_DEBUG:
        test_args.append('+d')
    self.run_batch(script, *test_args, *self.tests)
