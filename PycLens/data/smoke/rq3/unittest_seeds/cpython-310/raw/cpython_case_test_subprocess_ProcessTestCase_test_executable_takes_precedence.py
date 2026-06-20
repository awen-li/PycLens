# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_executable_takes_precedence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pre_args = [sys.executable, '-c']
    self._assert_python(pre_args)
    self.assertRaises(NONEXISTING_ERRORS, self._assert_python, pre_args, executable=NONEXISTING_CMD[0])
