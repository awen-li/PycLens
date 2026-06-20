# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_exists_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = os.pipe()
    try:
        self.assertTrue(self.pathmodule.exists(r))
    finally:
        os.close(r)
        os.close(w)
    self.assertFalse(self.pathmodule.exists(r))
