# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_lone_surrogates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            with self.assertRaises(UnicodeEncodeError):
                plistlib.dumps('\ud8ff', fmt=fmt)
            with self.assertRaises(UnicodeEncodeError):
                plistlib.dumps('\udcff', fmt=fmt)
