# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_invalid_string_prefixes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    single_quote_cases = ["fu''", "uf''", "Fu''", "fU''", "Uf''", "uF''", "ufr''", "urf''", "fur''", "fru''", "rfu''", "ruf''", "FUR''", "Fur''", "fb''", "fB''", "Fb''", "FB''", "bf''", "bF''", "Bf''", "BF''"]
    double_quote_cases = [case.replace("'", '"') for case in single_quote_cases]
    self.assertAllRaise(SyntaxError, 'invalid syntax', single_quote_cases + double_quote_cases)
