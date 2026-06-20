# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_check_output_stderr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output = subprocess.check_output([sys.executable, '-c', "import sys; sys.stderr.write('BDFL')"], stderr=subprocess.STDOUT)
    self.assertIn(b'BDFL', output)
