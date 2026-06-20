# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_bytesio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            b = BytesIO()
            pl = self._create(fmt=fmt)
            plistlib.dump(pl, b, fmt=fmt)
            pl2 = plistlib.load(BytesIO(b.getvalue()), fmt=fmt)
            self.assertEqual(dict(pl), dict(pl2))
            pl2 = plistlib.load(BytesIO(b.getvalue()))
            self.assertEqual(dict(pl), dict(pl2))
