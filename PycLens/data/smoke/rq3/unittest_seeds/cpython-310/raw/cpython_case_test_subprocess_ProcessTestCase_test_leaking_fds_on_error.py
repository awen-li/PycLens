# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_leaking_fds_on_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(1024):
        with self.assertRaises(NONEXISTING_ERRORS):
            subprocess.Popen(NONEXISTING_CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
