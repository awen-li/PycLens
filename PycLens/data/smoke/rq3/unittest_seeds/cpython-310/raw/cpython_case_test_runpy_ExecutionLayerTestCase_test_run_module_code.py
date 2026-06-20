# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: ExecutionLayerTestCase_test_run_module_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod_name = '<Nonsense>'
    mod_fname = 'Some other nonsense'
    mod_loader = "Now you're just being silly"
    mod_package = ''
    mod_spec = importlib.machinery.ModuleSpec(mod_name, origin=mod_fname, loader=mod_loader)
    expected_ns = example_namespace.copy()
    expected_ns.update({'__name__': mod_name, '__file__': mod_fname, '__loader__': mod_loader, '__package__': mod_package, '__spec__': mod_spec, 'run_argv0': mod_fname, 'run_name_in_sys_modules': True, 'module_in_sys_modules': True})

    def create_ns(init_globals):
        return _run_module_code(example_source, init_globals, mod_name, mod_spec)
    self.check_code_execution(create_ns, expected_ns)
