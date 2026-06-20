# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: TokenTests_test_float_exponent_tokenization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        self.assertEqual(eval('1 if 1else 0'), 1)
        self.assertEqual(eval('1 if 0else 0'), 0)
    self.assertRaises(SyntaxError, eval, '0 if 1Else 0')
