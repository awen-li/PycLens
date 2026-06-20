# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_pathlike_executable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    doesnotexist = os.path.join(os.path.dirname(sys.executable), 'doesnotexist')
    self._assert_python([doesnotexist, '-c'], executable=FakePath(sys.executable))
