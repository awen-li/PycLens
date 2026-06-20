# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_create_builtin_subinterp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import builtins
    create_builtin = support.get_attribute(_imp, 'create_builtin')

    class Spec:
        name = 'builtins'
    spec = Spec()

    def check_get_builtins():
        refcnt = sys.getrefcount(builtins)
        mod = _imp.create_builtin(spec)
        self.assertIs(mod, builtins)
        self.assertEqual(sys.getrefcount(builtins), refcnt + 1)
        gc.collect()
    check_get_builtins()
    ret = support.run_in_subinterp('import builtins')
    self.assertEqual(ret, 0)
    check_get_builtins()
