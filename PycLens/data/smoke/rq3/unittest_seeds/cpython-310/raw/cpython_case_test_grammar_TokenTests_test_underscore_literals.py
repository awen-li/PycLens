# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: TokenTests_test_underscore_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for lit in VALID_UNDERSCORE_LITERALS:
        self.assertEqual(eval(lit), eval(lit.replace('_', '')))
    for lit in INVALID_UNDERSCORE_LITERALS:
        self.assertRaises(SyntaxError, eval, lit)
    self.assertRaises(NameError, eval, '_0')
