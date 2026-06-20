# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_assert_syntax_warnings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_syntax_warning('assert(x, "msg")', 'assertion is always true')
    self.check_syntax_warning('assert(False, "msg")', 'assertion is always true')
    self.check_syntax_warning('assert(False,)', 'assertion is always true')
    with self.check_no_warnings(category=SyntaxWarning):
        compile('assert x, "msg"', '<testcase>', 'exec')
        compile('assert False, "msg"', '<testcase>', 'exec')
