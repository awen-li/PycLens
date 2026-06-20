# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_no_backslashes_in_expression_part

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAllRaise(SyntaxError, 'f-string expression part cannot include a backslash', ["f'{\\'a\\'}'", "f'{\\t3}'", "f'{\\}'", "rf'{\\'a\\'}'", "rf'{\\t3}'", "rf'{\\}'", 'rf\'{"\\N{LEFT CURLY BRACKET}"}\'', "f'{\\n}'"])
