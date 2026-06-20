# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestBinaryPlistlib_test_large_timestamp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for ts in (-2 ** 31 - 1, 2 ** 31):
        with self.subTest(ts=ts):
            d = datetime.datetime.utcfromtimestamp(0) + datetime.timedelta(seconds=ts)
            data = plistlib.dumps(d, fmt=plistlib.FMT_BINARY)
            self.assertEqual(plistlib.loads(data), d)
