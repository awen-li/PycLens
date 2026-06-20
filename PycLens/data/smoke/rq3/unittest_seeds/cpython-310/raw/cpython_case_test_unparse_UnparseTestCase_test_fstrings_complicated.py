# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_fstrings_complicated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_ast_roundtrip('f\'\'\'{"\'"}\'\'\'')
    self.check_ast_roundtrip('f\'\'\'-{f"""*{f"+{f\'.{x}.\'}+"}*"""}-\'\'\'')
    self.check_ast_roundtrip('f\'\'\'-{f"""*{f"+{f\'.{x}.\'}+"}*"""}-\'single quote\\\'\'\'\'')
    self.check_ast_roundtrip('f"""{\'\'\'\n\'\'\'}"""')
    self.check_ast_roundtrip('f"""{g(\'\'\'\n\'\'\')}"""')
    self.check_ast_roundtrip('f"a\\r\\nb"')
    self.check_ast_roundtrip('f"\\u2028{\'x\'}"')
