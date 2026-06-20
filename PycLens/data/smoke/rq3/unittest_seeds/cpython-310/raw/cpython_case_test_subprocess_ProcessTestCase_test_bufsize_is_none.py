# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_bufsize_is_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen(ZERO_RETURN_CMD, None)
    self.assertEqual(p.wait(), 0)
    p = subprocess.Popen(ZERO_RETURN_CMD, bufsize=None)
    self.assertEqual(p.wait(), 0)
