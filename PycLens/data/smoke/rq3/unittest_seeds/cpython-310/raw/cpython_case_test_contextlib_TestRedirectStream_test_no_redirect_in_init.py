# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestRedirectStream_test_no_redirect_in_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig_stdout = getattr(sys, self.orig_stream)
    self.redirect_stream(None)
    self.assertIs(getattr(sys, self.orig_stream), orig_stdout)
