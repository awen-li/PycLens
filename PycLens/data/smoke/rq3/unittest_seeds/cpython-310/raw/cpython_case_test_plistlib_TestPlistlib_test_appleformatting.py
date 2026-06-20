# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_appleformatting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            pl = plistlib.loads(TESTDATA[fmt])
            data = plistlib.dumps(pl, fmt=fmt)
            self.assertEqual(data, TESTDATA[fmt], "generated data was not identical to Apple's output")
