# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestBinaryPlistlib_test_dump_duplicates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (None, False, True, 12345, 123.45, 'abcde', 'абвгд', b'abcde', datetime.datetime(2004, 10, 26, 10, 33, 33), bytearray(b'abcde'), [12, 345], (12, 345), {'12': 345}):
        with self.subTest(x=x):
            data = plistlib.dumps([x] * 1000, fmt=plistlib.FMT_BINARY)
            self.assertLess(len(data), 1100, repr(data))
