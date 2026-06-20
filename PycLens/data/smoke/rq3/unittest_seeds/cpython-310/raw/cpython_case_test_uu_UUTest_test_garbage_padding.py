# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUTest_test_garbage_padding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodedtext1 = b'begin 644 file\n!,___\n \nend\n'
    encodedtext2 = b'begin 644 file\n!,___\n`\nend\n'
    plaintext = b'3'
    for encodedtext in (encodedtext1, encodedtext2):
        with self.subTest('uu.decode()'):
            inp = io.BytesIO(encodedtext)
            out = io.BytesIO()
            uu.decode(inp, out, quiet=True)
            self.assertEqual(out.getvalue(), plaintext)
        with self.subTest('uu_codec'):
            import codecs
            decoded = codecs.decode(encodedtext, 'uu_codec')
            self.assertEqual(decoded, plaintext)
