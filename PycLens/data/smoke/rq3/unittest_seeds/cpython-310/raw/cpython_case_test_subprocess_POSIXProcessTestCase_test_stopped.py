# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_stopped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = ZERO_RETURN_CMD
    proc = subprocess.Popen(args)
    support.wait_process(proc.pid, exitcode=0)
    status = _testcapi.W_STOPCODE(3)
    with mock.patch('subprocess.os.waitpid', return_value=(proc.pid, status)):
        returncode = proc.wait()
    self.assertEqual(returncode, -3)
