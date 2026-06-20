# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_chained_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_ast_roundtrip('1 < 4 <= 5')
    self.check_ast_roundtrip('a is b is c is not d')
