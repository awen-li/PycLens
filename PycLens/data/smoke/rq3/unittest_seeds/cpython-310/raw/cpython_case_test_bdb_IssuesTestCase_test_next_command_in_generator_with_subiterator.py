# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: IssuesTestCase_test_next_command_in_generator_with_subiterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\n            def test_subgen():\n                yield 0\n                return 123\n\n            def test_gen():\n                x = yield from test_subgen()\n                return 456\n\n            def main():\n                for i in test_gen():\n                    lno = 12\n                lno = 13\n        '
    modules = {TEST_MODULE: code}
    with create_modules(modules):
        self.expect_set = [('line', 2, 'tfunc_import'), break_in_func('test_gen', TEST_MODULE_FNAME), ('None', 2, 'tfunc_import'), ('continue',), ('line', 7, 'test_gen', ({1: 1}, [])), ('next',), ('line', 8, 'test_gen'), ('next',), ('exception', 11, 'main', StopIteration), ('step',), ('line', 13, 'main'), ('quit',)]
        with TracerRun(self) as tracer:
            tracer.runcall(tfunc_import)
