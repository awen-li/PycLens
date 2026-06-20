# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: IssuesTestCase_test_step_at_return_with_no_trace_in_caller

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code_1 = '\n            from test_module_for_bdb_2 import func\n            def main():\n                func()\n                lno = 5\n        '
    code_2 = '\n            def func():\n                lno = 3\n        '
    modules = {TEST_MODULE: code_1, 'test_module_for_bdb_2': code_2}
    with create_modules(modules):
        self.expect_set = [('line', 2, 'tfunc_import'), break_in_func('func', 'test_module_for_bdb_2.py'), ('None', 2, 'tfunc_import'), ('continue',), ('line', 3, 'func', ({1: 1}, [])), ('step',), ('return', 3, 'func'), ('step',), ('line', 5, 'main'), ('quit',)]
        with TracerRun(self) as tracer:
            tracer.runcall(tfunc_import)
