# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: Win32ProcessTestCase_test_close_fds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rc = subprocess.call([sys.executable, '-c', 'import sys; sys.exit(47)'], close_fds=True)
    self.assertEqual(rc, 47)
