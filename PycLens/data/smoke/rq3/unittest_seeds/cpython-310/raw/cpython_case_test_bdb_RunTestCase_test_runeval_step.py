# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: RunTestCase_test_runeval_step

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\n            def main():\n                lno = 3\n        '
    modules = {TEST_MODULE: code}
    with create_modules(modules):
        self.expect_set = [('line', 1, '<module>'), ('step',), ('call', 2, 'main'), ('step',), ('line', 3, 'main'), ('step',), ('return', 3, 'main'), ('step',), ('return', 1, '<module>'), ('quit',)]
        import test_module_for_bdb
        with TracerRun(self) as tracer:
            tracer.runeval('test_module_for_bdb.main()', globals(), locals())
