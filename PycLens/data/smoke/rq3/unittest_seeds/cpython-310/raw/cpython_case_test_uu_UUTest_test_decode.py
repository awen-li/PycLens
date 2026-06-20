# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUTest_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for backtick in (True, False):
        inp = io.BytesIO(encodedtextwrapped(438, 't1', backtick=backtick))
        out = io.BytesIO()
        uu.decode(inp, out)
        self.assertEqual(out.getvalue(), plaintext)
        inp = io.BytesIO(b'UUencoded files may contain many lines,\n' + b"even some that have 'begin' in them.\n" + encodedtextwrapped(438, 't1', backtick=backtick))
        out = io.BytesIO()
        uu.decode(inp, out)
        self.assertEqual(out.getvalue(), plaintext)
