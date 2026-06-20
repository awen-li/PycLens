# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_stderr_devnull

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys\nfor i in range(10240):sys.stderr.write("x" * 1024)'], stderr=subprocess.DEVNULL)
    p.wait()
    self.assertEqual(p.stderr, None)
