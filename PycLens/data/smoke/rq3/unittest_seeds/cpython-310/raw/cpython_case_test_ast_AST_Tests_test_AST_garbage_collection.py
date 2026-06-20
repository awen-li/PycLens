# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_AST_garbage_collection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:
        pass
    a = ast.AST()
    a.x = X()
    a.x.a = a
    ref = weakref.ref(a.x)
    del a
    support.gc_collect()
    self.assertIsNone(ref())
