# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_stdout_stderr_pipe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys;sys.stdout.write("apple");sys.stdout.flush();sys.stderr.write("orange")'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    with p:
        self.assertEqual(p.stdout.read(), b'appleorange')
