# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestExecutablePrependedZip_test_execute_zip2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output = subprocess.check_output([self.exe_zip, sys.executable])
    self.assertIn(b'number in executable: 5', output)
