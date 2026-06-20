# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_stderr_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'print("banana")'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    self.addCleanup(p.stdout.close)
    self.addCleanup(p.stdin.close)
    p.wait()
    self.assertEqual(p.stderr, None)
