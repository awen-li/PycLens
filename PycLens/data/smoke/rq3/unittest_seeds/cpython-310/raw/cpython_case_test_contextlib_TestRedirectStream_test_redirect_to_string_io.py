# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestRedirectStream_test_redirect_to_string_io

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.StringIO()
    msg = 'Consider an API like help(), which prints directly to stdout'
    orig_stdout = getattr(sys, self.orig_stream)
    with self.redirect_stream(f):
        print(msg, file=getattr(sys, self.orig_stream))
    self.assertIs(getattr(sys, self.orig_stream), orig_stdout)
    s = f.getvalue().strip()
    self.assertEqual(s, msg)
