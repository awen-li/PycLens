# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_fstrings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_ast_roundtrip('f\'{f"{0}"*3}\'')
    self.check_ast_roundtrip('f\'{f"{y}"*3}\'')
    self.check_ast_roundtrip("f''")
    self.check_ast_roundtrip('f"""\'end\' "quote\\""""')
