# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_syntax_error_for_starred_expressions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    error_msg = re.escape('cannot use starred expression here')
    with self.assertRaisesRegex(SyntaxError, error_msg):
        compile("f'{*a}'", '?', 'exec')
    error_msg = re.escape('cannot use double starred expression here')
    with self.assertRaisesRegex(SyntaxError, error_msg):
        compile("f'{**a}'", '?', 'exec')
