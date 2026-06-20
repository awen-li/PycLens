# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_communicate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;sys.stderr.write("pineapple");sys.stdout.write(sys.stdin.read())'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    self.addCleanup(p.stdout.close)
    self.addCleanup(p.stderr.close)
    self.addCleanup(p.stdin.close)
    (stdout, stderr) = p.communicate(b'banana')
    self.assertEqual(stdout, b'banana')
    self.assertEqual(stderr, b'pineapple')
