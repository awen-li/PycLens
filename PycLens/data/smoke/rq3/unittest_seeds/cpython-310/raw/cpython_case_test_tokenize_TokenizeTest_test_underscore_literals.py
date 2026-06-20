# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_underscore_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def number_token(s):
        f = BytesIO(s.encode('utf-8'))
        for (toktype, token, start, end, line) in tokenize(f.readline):
            if toktype == NUMBER:
                return token
        return 'invalid token'
    for lit in VALID_UNDERSCORE_LITERALS:
        if '(' in lit:
            continue
        self.assertEqual(number_token(lit), lit)
    for lit in INVALID_UNDERSCORE_LITERALS:
        self.assertNotEqual(number_token(lit), lit)
