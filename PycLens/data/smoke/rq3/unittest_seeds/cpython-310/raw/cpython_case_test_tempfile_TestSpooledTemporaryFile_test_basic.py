# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.do_create()
    self.assertFalse(f._rolled)
    f = self.do_create(max_size=100, pre='a', suf='.txt')
    self.assertFalse(f._rolled)
