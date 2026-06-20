# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestRedirectStream_test_enter_result_is_target

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.StringIO()
    with self.redirect_stream(f) as enter_result:
        self.assertIs(enter_result, f)
