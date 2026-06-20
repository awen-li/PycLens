# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_stderr_redirect_with_no_stdout_redirect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys, subprocess;rc = subprocess.call([sys.executable, "-c",    "import sys;"    "sys.stderr.write(\'42\')"],    stderr=subprocess.STDOUT);sys.exit(rc)'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    self.assertEqual(stdout, b'42')
    self.assertEqual(stderr, b'')
    self.assertEqual(p.returncode, 0)
