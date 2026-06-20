# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_executable_with_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (python_dir, python_base) = self._split_python_path()
    python_dir = self._normalize_cwd(python_dir)
    self._assert_cwd(python_dir, 'somethingyoudonthave', executable=sys.executable, cwd=python_dir)
