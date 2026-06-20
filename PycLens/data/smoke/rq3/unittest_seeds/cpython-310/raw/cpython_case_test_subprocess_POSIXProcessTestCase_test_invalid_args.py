# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_invalid_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, subprocess.call, [sys.executable, '-c', 'import sys; sys.exit(47)'], startupinfo=47)
    self.assertRaises(ValueError, subprocess.call, [sys.executable, '-c', 'import sys; sys.exit(47)'], creationflags=47)
