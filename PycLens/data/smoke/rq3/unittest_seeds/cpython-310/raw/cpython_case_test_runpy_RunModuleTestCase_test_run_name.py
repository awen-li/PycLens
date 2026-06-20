# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunModuleTestCase_test_run_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    depth = 1
    run_name = 'And now for something completely different'
    (pkg_dir, mod_fname, mod_name, mod_spec) = self._make_pkg(example_source, depth)
    forget(mod_name)
    expected_ns = example_namespace.copy()
    expected_ns.update({'__name__': run_name, '__file__': mod_fname, '__cached__': importlib.util.cache_from_source(mod_fname), '__package__': mod_name.rpartition('.')[0], '__spec__': mod_spec})

    def create_ns(init_globals):
        return run_module(mod_name, init_globals, run_name)
    try:
        self.check_code_execution(create_ns, expected_ns)
    finally:
        self._del_pkg(pkg_dir)
