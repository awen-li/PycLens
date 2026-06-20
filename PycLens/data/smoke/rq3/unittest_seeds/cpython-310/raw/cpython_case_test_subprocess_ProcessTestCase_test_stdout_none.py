# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_stdout_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys; from subprocess import Popen, PIPE;p = Popen([sys.executable, "-c", "print(\'test_stdout_none\')"],          stdin=PIPE, stderr=PIPE);p.wait(); assert p.stdout is None;'
    p = subprocess.Popen([sys.executable, '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    self.addCleanup(p.stdout.close)
    self.addCleanup(p.stderr.close)
    (out, err) = p.communicate()
    self.assertEqual(p.returncode, 0, err)
    self.assertEqual(out.rstrip(), b'test_stdout_none')
