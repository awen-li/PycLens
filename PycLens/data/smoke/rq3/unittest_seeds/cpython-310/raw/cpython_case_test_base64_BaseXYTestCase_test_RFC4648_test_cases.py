# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_RFC4648_test_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b64encode = base64.b64encode
    b32hexencode = base64.b32hexencode
    b32encode = base64.b32encode
    b16encode = base64.b16encode
    self.assertEqual(b64encode(b''), b'')
    self.assertEqual(b64encode(b'f'), b'Zg==')
    self.assertEqual(b64encode(b'fo'), b'Zm8=')
    self.assertEqual(b64encode(b'foo'), b'Zm9v')
    self.assertEqual(b64encode(b'foob'), b'Zm9vYg==')
    self.assertEqual(b64encode(b'fooba'), b'Zm9vYmE=')
    self.assertEqual(b64encode(b'foobar'), b'Zm9vYmFy')
    self.assertEqual(b32encode(b''), b'')
    self.assertEqual(b32encode(b'f'), b'MY======')
    self.assertEqual(b32encode(b'fo'), b'MZXQ====')
    self.assertEqual(b32encode(b'foo'), b'MZXW6===')
    self.assertEqual(b32encode(b'foob'), b'MZXW6YQ=')
    self.assertEqual(b32encode(b'fooba'), b'MZXW6YTB')
    self.assertEqual(b32encode(b'foobar'), b'MZXW6YTBOI======')
    self.assertEqual(b32hexencode(b''), b'')
    self.assertEqual(b32hexencode(b'f'), b'CO======')
    self.assertEqual(b32hexencode(b'fo'), b'CPNG====')
    self.assertEqual(b32hexencode(b'foo'), b'CPNMU===')
    self.assertEqual(b32hexencode(b'foob'), b'CPNMUOG=')
    self.assertEqual(b32hexencode(b'fooba'), b'CPNMUOJ1')
    self.assertEqual(b32hexencode(b'foobar'), b'CPNMUOJ1E8======')
    self.assertEqual(b16encode(b''), b'')
    self.assertEqual(b16encode(b'f'), b'66')
    self.assertEqual(b16encode(b'fo'), b'666F')
    self.assertEqual(b16encode(b'foo'), b'666F6F')
    self.assertEqual(b16encode(b'foob'), b'666F6F62')
    self.assertEqual(b16encode(b'fooba'), b'666F6F6261')
    self.assertEqual(b16encode(b'foobar'), b'666F6F626172')
