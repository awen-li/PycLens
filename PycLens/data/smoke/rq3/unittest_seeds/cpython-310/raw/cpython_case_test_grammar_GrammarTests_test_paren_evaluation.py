# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_paren_evaluation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(16 // (4 // 2), 8)
    self.assertEqual(16 // 4 // 2, 2)
    self.assertEqual(16 // 4 // 2, 2)
    x = 2
    y = 3
    self.assertTrue(False is (x is y))
    self.assertFalse((False is x) is y)
    self.assertFalse(False is x is y)
