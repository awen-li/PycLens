# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: LegacyBase64TestCase_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from io import BytesIO, StringIO
    infp = BytesIO(b'd3d3LnB5dGhvbi5vcmc=')
    outfp = BytesIO()
    base64.decode(infp, outfp)
    self.assertEqual(outfp.getvalue(), b'www.python.org')
    self.assertRaises(TypeError, base64.encode, StringIO('YWJj\n'), BytesIO())
    self.assertRaises(TypeError, base64.encode, BytesIO(b'YWJj\n'), StringIO())
    self.assertRaises(TypeError, base64.encode, StringIO('YWJj\n'), StringIO())
