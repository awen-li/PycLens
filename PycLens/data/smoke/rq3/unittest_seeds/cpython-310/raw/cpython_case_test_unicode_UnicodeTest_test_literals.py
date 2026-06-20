# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('ÿ', 'ÿ')
    self.assertEqual('\uffff', '\uffff')
    self.assertRaises(SyntaxError, eval, "'\\Ufffffffe'")
    self.assertRaises(SyntaxError, eval, "'\\Uffffffff'")
    self.assertRaises(SyntaxError, eval, "'\\U%08x'" % 1114112)
    self.assertNotEqual('\\u0020', ' ')
