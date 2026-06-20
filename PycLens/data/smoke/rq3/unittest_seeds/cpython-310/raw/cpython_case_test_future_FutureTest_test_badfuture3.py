# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: FutureTest_test_badfuture3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(SyntaxError) as cm:
        from test import badsyntax_future3
    self.check_syntax_error(cm.exception, 'badsyntax_future3', 3)
