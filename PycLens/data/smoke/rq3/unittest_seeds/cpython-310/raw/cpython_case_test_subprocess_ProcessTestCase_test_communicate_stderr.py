# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_communicate_stderr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys; sys.stderr.write("pineapple")'], stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    self.assertEqual(stdout, None)
    self.assertEqual(stderr, b'pineapple')
