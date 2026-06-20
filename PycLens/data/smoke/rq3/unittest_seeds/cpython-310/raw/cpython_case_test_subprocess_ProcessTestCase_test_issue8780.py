# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_issue8780

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = ';'.join(('import subprocess, sys', 'retcode = subprocess.call([sys.executable, \'-c\', \'print("Hello World!")\'])', 'assert retcode == 0'))
    output = subprocess.check_output([sys.executable, '-c', code])
    self.assertTrue(output.startswith(b'Hello World!'), ascii(output))
