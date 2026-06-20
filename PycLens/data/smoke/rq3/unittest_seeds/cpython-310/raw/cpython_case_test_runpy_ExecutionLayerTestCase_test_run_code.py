# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: ExecutionLayerTestCase_test_run_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_ns = example_namespace.copy()
    expected_ns.update({'__loader__': None})

    def create_ns(init_globals):
        return _run_code(example_source, {}, init_globals)
    self.check_code_execution(create_ns, expected_ns)
