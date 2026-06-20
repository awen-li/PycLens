# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_failed_child_execute_fd_leak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd_directory = '/proc/%d/fd' % os.getpid()
    fds_before_popen = os.listdir(fd_directory)
    with self.assertRaises(PopenTestException):
        PopenExecuteChildRaises(ZERO_RETURN_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    fds_after_exception = os.listdir(fd_directory)
    self.assertEqual(fds_before_popen, fds_after_exception)
