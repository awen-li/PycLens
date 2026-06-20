# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: BreakpointTestCase_test_bp_after_last_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\n            def main():\n                lno = 3\n        '
    modules = {TEST_MODULE: code}
    with create_modules(modules):
        self.expect_set = [('line', 2, 'tfunc_import'), ('break', (TEST_MODULE_FNAME, 4))]
        with TracerRun(self) as tracer:
            self.assertRaises(BdbError, tracer.runcall, tfunc_import)
