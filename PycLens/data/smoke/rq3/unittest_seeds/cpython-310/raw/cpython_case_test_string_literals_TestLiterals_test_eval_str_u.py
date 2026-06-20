# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string_literals.py
# case: TestLiterals_test_eval_str_u

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(eval(" u'x' "), 'x')
    self.assertEqual(eval(" U'ä' "), 'ä')
    self.assertEqual(eval(" u'ä' "), 'ä')
    self.assertRaises(SyntaxError, eval, " ur'' ")
    self.assertRaises(SyntaxError, eval, " ru'' ")
    self.assertRaises(SyntaxError, eval, " bu'' ")
    self.assertRaises(SyntaxError, eval, " ub'' ")
