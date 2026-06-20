# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: IssuesTestCase_test_next_until_return_in_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\n            def test_gen():\n                yield 0\n                lno = 4\n                return 123\n\n            def main():\n                it = test_gen()\n                next(it)\n                next(it)\n                lno = 11\n        '
    modules = {TEST_MODULE: code}
    for set_type in ('next', 'until', 'return'):
        with self.subTest(set_type=set_type):
            with create_modules(modules):
                self.expect_set = [('line', 2, 'tfunc_import'), break_in_func('test_gen', TEST_MODULE_FNAME), ('None', 2, 'tfunc_import'), ('continue',), ('line', 3, 'test_gen', ({1: 1}, [])), (set_type,)]
                if set_type == 'return':
                    self.expect_set.extend([('exception', 10, 'main', StopIteration), ('step',), ('return', 10, 'main'), ('quit',)])
                else:
                    self.expect_set.extend([('line', 4, 'test_gen'), ('quit',)])
                with TracerRun(self) as tracer:
                    tracer.runcall(tfunc_import)
