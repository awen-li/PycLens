# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_send_signal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self._kill_process('send_signal', signal.SIGINT)
    (_, stderr) = p.communicate()
    self.assertIn(b'KeyboardInterrupt', stderr)
    self.assertNotEqual(p.wait(), 0)
