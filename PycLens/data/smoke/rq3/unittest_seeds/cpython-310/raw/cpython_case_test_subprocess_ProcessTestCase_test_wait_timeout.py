# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_wait_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(0.3)'])
    with self.assertRaises(subprocess.TimeoutExpired) as c:
        p.wait(timeout=0.0001)
    self.assertIn('0.0001', str(c.exception))
    self.assertEqual(p.wait(timeout=support.SHORT_TIMEOUT), 0)
