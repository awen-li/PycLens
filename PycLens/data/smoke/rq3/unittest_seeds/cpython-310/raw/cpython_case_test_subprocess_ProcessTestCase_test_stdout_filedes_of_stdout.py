# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_stdout_filedes_of_stdout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys, subprocess; rc = subprocess.call([sys.executable, "-c",     "import os, sys; sys.exit(os.write(sys.stdout.fileno(), b\'test with stdout=1\'))"], stdout=1); assert rc == 18'
    p = subprocess.Popen([sys.executable, '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    self.addCleanup(p.stdout.close)
    self.addCleanup(p.stderr.close)
    (out, err) = p.communicate()
    self.assertEqual(p.returncode, 0, err)
    self.assertEqual(out.rstrip(), b'test with stdout=1')
