# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_check_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cp = subprocess.run(ZERO_RETURN_CMD, check=True)
    self.assertEqual(cp.returncode, 0)
