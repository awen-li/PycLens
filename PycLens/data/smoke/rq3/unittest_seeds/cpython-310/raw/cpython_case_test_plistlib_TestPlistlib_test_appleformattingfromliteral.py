# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_appleformattingfromliteral

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.maxDiff = None
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            pl = self._create(fmt=fmt)
            pl2 = plistlib.loads(TESTDATA[fmt], fmt=fmt)
            self.assertEqual(dict(pl), dict(pl2), "generated data was not identical to Apple's output")
            pl2 = plistlib.loads(TESTDATA[fmt])
            self.assertEqual(dict(pl), dict(pl2), "generated data was not identical to Apple's output")
