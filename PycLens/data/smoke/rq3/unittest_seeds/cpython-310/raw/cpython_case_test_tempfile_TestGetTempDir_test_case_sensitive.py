# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestGetTempDir_test_case_sensitive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    case_sensitive_tempdir = tempfile.mkdtemp('-Temp')
    (_tempdir, tempfile.tempdir) = (tempfile.tempdir, None)
    try:
        with os_helper.EnvironmentVarGuard() as env:
            env['TMPDIR'] = case_sensitive_tempdir
            self.assertEqual(tempfile.gettempdir(), case_sensitive_tempdir)
    finally:
        tempfile.tempdir = _tempdir
        os_helper.rmdir(case_sensitive_tempdir)
