# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUTest_test_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inp = io.BytesIO(plaintext)
    out = io.BytesIO()
    uu.encode(inp, out, 't1')
    self.assertEqual(out.getvalue(), encodedtextwrapped(438, 't1'))
    inp = io.BytesIO(plaintext)
    out = io.BytesIO()
    uu.encode(inp, out, 't1', 420)
    self.assertEqual(out.getvalue(), encodedtextwrapped(420, 't1'))
    inp = io.BytesIO(plaintext)
    out = io.BytesIO()
    uu.encode(inp, out, 't1', backtick=True)
    self.assertEqual(out.getvalue(), encodedtextwrapped(438, 't1', True))
    with self.assertRaises(TypeError):
        uu.encode(inp, out, 't1', 420, True)
