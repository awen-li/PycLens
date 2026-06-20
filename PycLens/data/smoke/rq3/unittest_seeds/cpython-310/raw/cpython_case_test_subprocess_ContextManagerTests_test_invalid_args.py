# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ContextManagerTests_test_invalid_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(NONEXISTING_ERRORS):
        with subprocess.Popen(NONEXISTING_CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
            pass
