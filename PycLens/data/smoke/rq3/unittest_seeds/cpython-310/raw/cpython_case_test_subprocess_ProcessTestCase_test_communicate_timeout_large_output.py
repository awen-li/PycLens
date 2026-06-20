# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_communicate_timeout_large_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os,time;sys.stdout.write("a" * (64 * 1024));time.sleep(0.2);sys.stdout.write("a" * (64 * 1024));time.sleep(0.2);sys.stdout.write("a" * (64 * 1024));time.sleep(0.2);sys.stdout.write("a" * (64 * 1024));'], stdout=subprocess.PIPE)
    self.assertRaises(subprocess.TimeoutExpired, p.communicate, timeout=0.4)
    (stdout, _) = p.communicate()
    self.assertEqual(len(stdout), 4 * 64 * 1024)
