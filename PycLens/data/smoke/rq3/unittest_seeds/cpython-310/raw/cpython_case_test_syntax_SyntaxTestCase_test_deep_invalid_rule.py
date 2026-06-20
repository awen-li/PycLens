# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_deep_invalid_rule

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = 'd{{{{{{{{{{{{{{{{{{{{{{{{{```{{{{{{{ef f():y'
    with self.assertRaises(SyntaxError):
        compile(source, '<string>', 'exec')
