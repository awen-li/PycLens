# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_ast_roundtrip('def f(a : int): pass')
    self.check_ast_roundtrip('def f(a: int = 5): pass')
    self.check_ast_roundtrip('def f(*args: [int]): pass')
    self.check_ast_roundtrip('def f(**kwargs: dict): pass')
    self.check_ast_roundtrip('def f() -> None: pass')
