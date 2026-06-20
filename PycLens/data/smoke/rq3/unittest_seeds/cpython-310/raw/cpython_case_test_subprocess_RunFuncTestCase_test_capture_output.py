# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_capture_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cp = self.run_python("import sys;sys.stdout.write('BDFL'); sys.stderr.write('FLUFL')", capture_output=True)
    self.assertIn(b'BDFL', cp.stdout)
    self.assertIn(b'FLUFL', cp.stderr)
