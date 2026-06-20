# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestBinaryPlistlib_test_identity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (None, False, True, 12345, 123.45, 'abcde', b'abcde', datetime.datetime(2004, 10, 26, 10, 33, 33), bytearray(b'abcde'), [12, 345], (12, 345), {'12': 345}):
        with self.subTest(x=x):
            data = plistlib.dumps([x] * 2, fmt=plistlib.FMT_BINARY)
            (a, b) = plistlib.loads(data)
            if isinstance(x, tuple):
                x = list(x)
            self.assertEqual(a, x)
            self.assertEqual(b, x)
            self.assertIs(a, b)
