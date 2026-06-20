# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_non_bmp_characters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = {'python': '🐍'}
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            data = plistlib.dumps(pl, fmt=fmt)
            self.assertEqual(plistlib.loads(data), pl)
