# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: BreakpointTestCase_test_clear_two_bp_on_same_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\n            def func():\n                lno = 3\n                lno = 4\n\n            def main():\n                for i in range(3):\n                    func()\n        '
    modules = {TEST_MODULE: code}
    with create_modules(modules):
        self.expect_set = [('line', 2, 'tfunc_import'), ('break', (TEST_MODULE_FNAME, 3)), ('None', 2, 'tfunc_import'), ('break', (TEST_MODULE_FNAME, 3)), ('None', 2, 'tfunc_import'), ('break', (TEST_MODULE_FNAME, 4)), ('None', 2, 'tfunc_import'), ('continue',), ('line', 3, 'func', ({1: 1}, [])), ('continue',), ('line', 4, 'func', ({3: 1}, [])), ('clear', (TEST_MODULE_FNAME, 3)), ('None', 4, 'func'), ('continue',), ('line', 4, 'func', ({3: 2}, [])), ('quit',)]
        with TracerRun(self) as tracer:
            tracer.runcall(tfunc_import)
