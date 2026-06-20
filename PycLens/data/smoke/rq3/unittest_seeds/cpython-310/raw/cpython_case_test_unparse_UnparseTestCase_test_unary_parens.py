# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_unary_parens

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_ast_roundtrip('(-1)**7')
    self.check_ast_roundtrip('(-1.)**8')
    self.check_ast_roundtrip('(-1j)**6')
    self.check_ast_roundtrip('not True or False')
    self.check_ast_roundtrip('True or not False')
