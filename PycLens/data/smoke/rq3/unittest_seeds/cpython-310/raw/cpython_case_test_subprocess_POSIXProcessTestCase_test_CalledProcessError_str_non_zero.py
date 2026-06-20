# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_CalledProcessError_str_non_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    err = subprocess.CalledProcessError(2, 'fake cmd')
    error_string = str(err)
    self.assertIn('non-zero exit status 2.', error_string)
