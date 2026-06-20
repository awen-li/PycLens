# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string_literals.py
# case: TestLiterals_test_eval_str_incomplete

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(SyntaxError, eval, " '\\x' ")
    self.assertRaises(SyntaxError, eval, " '\\x0' ")
    self.assertRaises(SyntaxError, eval, " '\\u' ")
    self.assertRaises(SyntaxError, eval, " '\\u0' ")
    self.assertRaises(SyntaxError, eval, " '\\u00' ")
    self.assertRaises(SyntaxError, eval, " '\\u000' ")
    self.assertRaises(SyntaxError, eval, " '\\U' ")
    self.assertRaises(SyntaxError, eval, " '\\U0' ")
    self.assertRaises(SyntaxError, eval, " '\\U00' ")
    self.assertRaises(SyntaxError, eval, " '\\U000' ")
    self.assertRaises(SyntaxError, eval, " '\\U0000' ")
    self.assertRaises(SyntaxError, eval, " '\\U00000' ")
    self.assertRaises(SyntaxError, eval, " '\\U000000' ")
    self.assertRaises(SyntaxError, eval, " '\\U0000000' ")
