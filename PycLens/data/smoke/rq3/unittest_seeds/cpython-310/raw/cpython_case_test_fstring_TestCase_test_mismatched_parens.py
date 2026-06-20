# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_mismatched_parens

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\}' does not match opening parenthesis '\\('", ["f'{((}'"])
    self.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\)' does not match opening parenthesis '\\['", ["f'{a[4)}'"])
    self.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\]' does not match opening parenthesis '\\('", ["f'{a(4]}'"])
    self.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\}' does not match opening parenthesis '\\['", ["f'{a[4}'"])
    self.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\}' does not match opening parenthesis '\\('", ["f'{a(4}'"])
    self.assertRaises(SyntaxError, eval, "f'{" + '(' * 500 + "}'")
