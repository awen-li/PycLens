# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_skipkeys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = {42: 'aNumber', 'snake': 'aWord'}
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            data = plistlib.dumps(pl, fmt=fmt, skipkeys=True, sort_keys=False)
            pl2 = plistlib.loads(data)
            self.assertEqual(pl2, {'snake': 'aWord'})
            fp = BytesIO()
            plistlib.dump(pl, fp, fmt=fmt, skipkeys=True, sort_keys=False)
            data = fp.getvalue()
            pl2 = plistlib.loads(fp.getvalue())
            self.assertEqual(pl2, {'snake': 'aWord'})
