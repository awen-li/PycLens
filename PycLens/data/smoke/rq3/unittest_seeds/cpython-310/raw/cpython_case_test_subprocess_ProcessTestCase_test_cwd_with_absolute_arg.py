# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_cwd_with_absolute_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (python_dir, python_base) = self._split_python_path()
    abs_python = os.path.join(python_dir, python_base)
    rel_python = os.path.join(os.curdir, python_base)
    with os_helper.temp_dir() as wrong_dir:
        self.assertRaises(FileNotFoundError, subprocess.Popen, [rel_python], cwd=wrong_dir)
        wrong_dir = self._normalize_cwd(wrong_dir)
        self._assert_cwd(wrong_dir, abs_python, cwd=wrong_dir)
