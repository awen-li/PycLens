# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: StateTestCase_test_skip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sys.meta_path[:] = (item for item in sys.meta_path if item.__module__.startswith('_frozen_importlib'))
    code = '\n            def main():\n                lno = 3\n        '
    modules = {TEST_MODULE: code}
    with create_modules(modules):
        self.expect_set = [('line', 2, 'tfunc_import'), ('step',), ('line', 3, 'tfunc_import'), ('quit',)]
        skip = ('importlib*', 'zipimport', 'encodings.*', TEST_MODULE)
        with TracerRun(self, skip=skip) as tracer:
            tracer.runcall(tfunc_import)
