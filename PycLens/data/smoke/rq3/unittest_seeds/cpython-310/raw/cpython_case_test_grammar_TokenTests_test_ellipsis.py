# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: TokenTests_test_ellipsis

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ...
    self.assertTrue(x is Ellipsis)
    self.assertRaises(SyntaxError, eval, '.. .')
