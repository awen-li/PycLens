# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ContextManagerTests_test_pipe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with subprocess.Popen([sys.executable, '-c', "import sys;sys.stdout.write('stdout');sys.stderr.write('stderr');"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        self.assertEqual(proc.stdout.read(), b'stdout')
        self.assertEqual(proc.stderr.read(), b'stderr')
    self.assertTrue(proc.stdout.closed)
    self.assertTrue(proc.stderr.closed)
