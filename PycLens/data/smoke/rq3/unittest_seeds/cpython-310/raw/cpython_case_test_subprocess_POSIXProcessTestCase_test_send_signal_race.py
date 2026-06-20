# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_send_signal_race

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    proc = subprocess.Popen(ZERO_RETURN_CMD)
    support.wait_process(proc.pid, exitcode=0)
    self.assertIsNone(proc.returncode)
    with mock.patch('os.kill') as mock_kill:
        proc.send_signal(signal.SIGTERM)
    mock_kill.assert_not_called()
    self.assertIsNotNone(proc.returncode)
