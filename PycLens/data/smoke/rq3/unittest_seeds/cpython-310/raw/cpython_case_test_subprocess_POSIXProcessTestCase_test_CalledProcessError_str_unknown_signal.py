# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_CalledProcessError_str_unknown_signal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    err = subprocess.CalledProcessError(-9876543, 'fake cmd')
    error_string = str(err)
    self.assertIn('unknown signal 9876543.', error_string)
