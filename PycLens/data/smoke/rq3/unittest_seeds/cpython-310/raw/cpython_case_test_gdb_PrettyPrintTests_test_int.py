# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertGdbRepr(42)
    self.assertGdbRepr(0)
    self.assertGdbRepr(-7)
    self.assertGdbRepr(1000000000000)
    self.assertGdbRepr(-1000000000000000)
