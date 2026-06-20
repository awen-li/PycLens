# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_keys_no_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = {42: 'aNumber'}
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            self.assertRaises(TypeError, plistlib.dumps, pl, fmt=fmt)
            b = BytesIO()
            self.assertRaises(TypeError, plistlib.dump, pl, b, fmt=fmt)
