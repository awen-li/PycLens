# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestRedirectStream_test_cm_is_reusable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.StringIO()
    write_to_f = self.redirect_stream(f)
    orig_stdout = getattr(sys, self.orig_stream)
    with write_to_f:
        print('Hello', end=' ', file=getattr(sys, self.orig_stream))
    with write_to_f:
        print('World!', file=getattr(sys, self.orig_stream))
    self.assertIs(getattr(sys, self.orig_stream), orig_stdout)
    s = f.getvalue()
    self.assertEqual(s, 'Hello World!\n')
