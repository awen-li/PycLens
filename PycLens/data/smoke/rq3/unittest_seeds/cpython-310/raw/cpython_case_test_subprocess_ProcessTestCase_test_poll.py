# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_poll

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import os; os.read(0, 1)'], stdin=subprocess.PIPE)
    self.addCleanup(p.stdin.close)
    self.assertIsNone(p.poll())
    os.write(p.stdin.fileno(), b'A')
    p.wait()
    self.assertEqual(p.poll(), 0)
