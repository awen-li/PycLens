# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for pl in [0, 2 ** 8 - 1, 2 ** 8, 2 ** 16 - 1, 2 ** 16, 2 ** 32 - 1, 2 ** 32, 2 ** 63 - 1, 2 ** 64 - 1, 1, -2 ** 63]:
        for fmt in ALL_FORMATS:
            with self.subTest(pl=pl, fmt=fmt):
                data = plistlib.dumps(pl, fmt=fmt)
                pl2 = plistlib.loads(data)
                self.assertIsInstance(pl2, int)
                self.assertEqual(pl, pl2)
                data2 = plistlib.dumps(pl2, fmt=fmt)
                self.assertEqual(data, data2)
    for fmt in ALL_FORMATS:
        for pl in (2 ** 64 + 1, 2 ** 127 - 1, -2 ** 64, -2 ** 127):
            with self.subTest(pl=pl, fmt=fmt):
                self.assertRaises(OverflowError, plistlib.dumps, pl, fmt=fmt)
