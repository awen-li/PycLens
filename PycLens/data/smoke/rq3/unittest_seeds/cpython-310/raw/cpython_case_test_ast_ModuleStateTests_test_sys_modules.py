# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ModuleStateTests_test_sys_modules

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lazy_mod = object()

    def my_import(name, *args, **kw):
        sys.modules[name] = lazy_mod
        return lazy_mod
    with support.swap_item(sys.modules, '_ast', None):
        del sys.modules['_ast']
        with support.swap_attr(builtins, '__import__', my_import):
            self.check_ast_module()
            self.assertNotIn('_ast', sys.modules)
            import _ast
            self.assertIs(_ast, lazy_mod)
