# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: BreakpointTestCase_test_clear_at_no_bp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.expect_set = [('line', 2, 'tfunc_import'), ('clear', (__file__, 1))]
    with TracerRun(self) as tracer:
        self.assertRaises(BdbError, tracer.runcall, tfunc_import)
