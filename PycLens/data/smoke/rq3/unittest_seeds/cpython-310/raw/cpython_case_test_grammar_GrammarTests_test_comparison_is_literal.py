# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_comparison_is_literal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(test, msg='"is" with a literal'):
        self.check_syntax_warning(test, msg)
    check('x is 1')
    check('x is "thing"')
    check('1 is x')
    check('x is y is 1')
    check('x is not 1', '"is not" with a literal')
    with warnings.catch_warnings():
        warnings.simplefilter('error', SyntaxWarning)
        compile('x is None', '<testcase>', 'exec')
        compile('x is False', '<testcase>', 'exec')
        compile('x is True', '<testcase>', 'exec')
        compile('x is ...', '<testcase>', 'exec')
