# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ModuleStateTests_test_reload_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.swap_item(sys.modules, '_ast', None):
        del sys.modules['_ast']
        import _ast as ast1
        del sys.modules['_ast']
        import _ast as ast2
        self.check_ast_module()
    del ast1
    del ast2
    support.gc_collect()
    self.check_ast_module()
