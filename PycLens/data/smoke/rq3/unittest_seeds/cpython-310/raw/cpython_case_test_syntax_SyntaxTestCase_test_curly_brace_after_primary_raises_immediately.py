# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_curly_brace_after_primary_raises_immediately

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_error('f{}', 'invalid syntax', mode='single')
