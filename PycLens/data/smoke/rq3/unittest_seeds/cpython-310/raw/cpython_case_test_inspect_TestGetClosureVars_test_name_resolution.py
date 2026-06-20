# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetClosureVars_test_name_resolution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(nonlocal_ref):

        def g(local_ref):
            print(local_ref, nonlocal_ref, _global_ref, unbound_ref)
        return g
    _arg = object()
    nonlocal_vars = {'nonlocal_ref': _arg}
    global_vars = {'_global_ref': _global_ref}
    builtin_vars = {'print': print}
    unbound_names = {'unbound_ref'}
    expected = inspect.ClosureVars(nonlocal_vars, global_vars, builtin_vars, unbound_names)
    self.assertEqual(inspect.getclosurevars(f(_arg)), expected)
