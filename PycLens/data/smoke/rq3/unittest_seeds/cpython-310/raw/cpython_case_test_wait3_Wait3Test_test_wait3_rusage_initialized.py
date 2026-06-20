# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wait3.py
# case: Wait3Test_test_wait3_rusage_initialized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = [sys.executable, '-c', 'import sys; sys.stdin.read()']
    proc = subprocess.Popen(args, stdin=subprocess.PIPE)
    try:
        (pid, status, rusage) = os.wait3(os.WNOHANG)
        self.assertEqual(0, pid)
        self.assertEqual(0, status)
        self.assertEqual(0, sum(rusage))
    finally:
        proc.stdin.close()
        proc.wait()
