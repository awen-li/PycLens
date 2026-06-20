# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_check_syntax_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.check_syntax_error(self, 'def class', lineno=1, offset=5)
    with self.assertRaises(AssertionError):
        support.check_syntax_error(self, 'x=1')
