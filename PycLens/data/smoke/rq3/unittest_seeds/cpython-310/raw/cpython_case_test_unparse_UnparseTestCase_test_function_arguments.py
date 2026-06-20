# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_function_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_ast_roundtrip('def f(): pass')
    self.check_ast_roundtrip('def f(a): pass')
    self.check_ast_roundtrip('def f(b = 2): pass')
    self.check_ast_roundtrip('def f(a, b): pass')
    self.check_ast_roundtrip('def f(a, b = 2): pass')
    self.check_ast_roundtrip('def f(a = 5, b = 2): pass')
    self.check_ast_roundtrip('def f(*, a = 1, b = 2): pass')
    self.check_ast_roundtrip('def f(*, a = 1, b): pass')
    self.check_ast_roundtrip('def f(*, a, b = 2): pass')
    self.check_ast_roundtrip('def f(a, b = None, *, c, **kwds): pass')
    self.check_ast_roundtrip('def f(a=2, *args, c=5, d, **kwds): pass')
    self.check_ast_roundtrip('def f(*args, **kwargs): pass')
