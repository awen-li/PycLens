# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_tuple_members

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = {'first': (1, 2), 'second': (1, 2), 'third': (3, 4)}
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            data = plistlib.dumps(pl, fmt=fmt)
            pl2 = plistlib.loads(data)
            self.assertEqual(pl2, {'first': [1, 2], 'second': [1, 2], 'third': [3, 4]})
            if fmt != plistlib.FMT_BINARY:
                self.assertIsNot(pl2['first'], pl2['second'])
