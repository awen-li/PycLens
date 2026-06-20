# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: CosmeticTestCase_test_fstrings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_src_roundtrip('f\'\'\'-{f"""*{f"+{f\'.{x}.\'}+"}*"""}-\'\'\'')
    self.check_src_roundtrip('f"\\u2028{\'x\'}"')
    self.check_src_roundtrip("f'{x}\\n'")
    self.check_src_roundtrip('f\'\'\'{"""\n"""}\\n\'\'\'')
    self.check_src_roundtrip('f\'\'\'{f"""{x}\n"""}\\n\'\'\'')
