# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_assert_warning_promotes_to_syntax_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings():
        warnings.simplefilter('error', SyntaxWarning)
        try:
            compile('assert x, "msg" ', '<testcase>', 'exec')
        except SyntaxError:
            self.fail('SyntaxError incorrectly raised for \'assert x, "msg"\'')
        with self.assertRaises(SyntaxError):
            compile('assert(x, "msg")', '<testcase>', 'exec')
        with self.assertRaises(SyntaxError):
            compile('assert(False, "msg")', '<testcase>', 'exec')
        with self.assertRaises(SyntaxError):
            compile('assert(False,)', '<testcase>', 'exec')
