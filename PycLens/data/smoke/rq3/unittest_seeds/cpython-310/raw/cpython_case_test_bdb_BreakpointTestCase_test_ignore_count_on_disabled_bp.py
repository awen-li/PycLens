# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: BreakpointTestCase_test_ignore_count_on_disabled_bp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\n            def func():\n                lno = 3\n\n            def main():\n                for i in range(3):\n                    func()\n        '
    modules = {TEST_MODULE: code}
    with create_modules(modules):
        self.expect_set = [('line', 2, 'tfunc_import'), break_in_func('func', TEST_MODULE_FNAME), ('None', 2, 'tfunc_import'), break_in_func('func', TEST_MODULE_FNAME), ('None', 2, 'tfunc_import'), ('ignore', (1,)), ('None', 2, 'tfunc_import'), ('disable', (1,)), ('None', 2, 'tfunc_import'), ('continue',), ('line', 3, 'func', ({2: 1}, [])), ('enable', (1,)), ('None', 3, 'func'), ('continue',), ('line', 3, 'func', ({2: 2}, [])), ('continue',), ('line', 3, 'func', ({1: 2}, [])), ('quit',)]
        with TracerRun(self) as tracer:
            tracer.runcall(tfunc_import)
