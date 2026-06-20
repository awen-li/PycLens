# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: IssuesTestCase_test_next_command_in_generator_for_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\n            def test_gen():\n                yield 0\n                lno = 4\n                yield 1\n                return 123\n\n            def main():\n                for i in test_gen():\n                    lno = 10\n                lno = 11\n        '
    modules = {TEST_MODULE: code}
    with create_modules(modules):
        self.expect_set = [('line', 2, 'tfunc_import'), break_in_func('test_gen', TEST_MODULE_FNAME), ('None', 2, 'tfunc_import'), ('continue',), ('line', 3, 'test_gen', ({1: 1}, [])), ('next',), ('line', 4, 'test_gen'), ('next',), ('line', 5, 'test_gen'), ('next',), ('line', 6, 'test_gen'), ('next',), ('exception', 9, 'main', StopIteration), ('step',), ('line', 11, 'main'), ('quit',)]
        with TracerRun(self) as tracer:
            tracer.runcall(tfunc_import)
