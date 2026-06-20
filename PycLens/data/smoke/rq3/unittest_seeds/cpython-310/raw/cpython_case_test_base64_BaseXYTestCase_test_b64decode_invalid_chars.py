# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b64decode_invalid_chars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = ((b'%3d==', b'\xdd'), (b'$3d==', b'\xdd'), (b'[==', b''), (b'YW]3=', b'am'), (b'3{d==', b'\xdd'), (b'3d}==', b'\xdd'), (b'@@', b''), (b'!', b''), (b'YWJj\n', b'abc'), (b'YWJj\nYWI=', b'abcab'))
    funcs = (base64.b64decode, base64.standard_b64decode, base64.urlsafe_b64decode)
    for (bstr, res) in tests:
        for func in funcs:
            with self.subTest(bstr=bstr, func=func):
                self.assertEqual(func(bstr), res)
                self.assertEqual(func(bstr.decode('ascii')), res)
        with self.assertRaises(binascii.Error):
            base64.b64decode(bstr, validate=True)
        with self.assertRaises(binascii.Error):
            base64.b64decode(bstr.decode('ascii'), validate=True)
    res = b'\xfb\xef\xbe\xff\xff\xff'
    self.assertEqual(base64.b64decode(b'++[[//]]', b'[]'), res)
    self.assertEqual(base64.urlsafe_b64decode(b'++--//__'), res)
