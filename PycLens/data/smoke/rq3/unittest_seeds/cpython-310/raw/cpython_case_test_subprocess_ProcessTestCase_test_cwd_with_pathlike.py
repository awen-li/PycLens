# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_cwd_with_pathlike

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    temp_dir = tempfile.gettempdir()
    temp_dir = self._normalize_cwd(temp_dir)
    self._assert_cwd(temp_dir, sys.executable, cwd=FakePath(temp_dir))
