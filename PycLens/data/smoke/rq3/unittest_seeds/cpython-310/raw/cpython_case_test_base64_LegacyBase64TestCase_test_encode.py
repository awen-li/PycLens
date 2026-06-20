# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: LegacyBase64TestCase_test_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    from io import BytesIO, StringIO
    infp = BytesIO(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}')
    outfp = BytesIO()
    base64.encode(infp, outfp)
    eq(outfp.getvalue(), b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0\nNTY3ODkhQCMwXiYqKCk7Ojw+LC4gW117fQ==\n')
    self.assertRaises(TypeError, base64.encode, StringIO('abc'), BytesIO())
    self.assertRaises(TypeError, base64.encode, BytesIO(b'abc'), StringIO())
    self.assertRaises(TypeError, base64.encode, StringIO('abc'), StringIO())
