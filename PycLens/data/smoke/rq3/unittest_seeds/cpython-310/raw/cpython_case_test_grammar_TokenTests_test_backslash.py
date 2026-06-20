# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: TokenTests_test_backslash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 1 + 1
    self.assertEqual(x, 2, 'backslash for line continuation')
    x = 0
    self.assertEqual(x, 0, 'backslash ending comment')
