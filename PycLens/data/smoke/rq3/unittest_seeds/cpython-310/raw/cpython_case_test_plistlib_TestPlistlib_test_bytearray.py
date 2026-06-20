# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_bytearray

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for pl in (b'<binary gunk>', b'<lots of binary gunk>\x00\x01\x02\x03' * 10):
        for fmt in ALL_FORMATS:
            with self.subTest(pl=pl, fmt=fmt):
                data = plistlib.dumps(bytearray(pl), fmt=fmt)
                pl2 = plistlib.loads(data)
                self.assertIsInstance(pl2, bytes)
                self.assertEqual(pl2, pl)
                data2 = plistlib.dumps(pl2, fmt=fmt)
                self.assertEqual(data, data2)
