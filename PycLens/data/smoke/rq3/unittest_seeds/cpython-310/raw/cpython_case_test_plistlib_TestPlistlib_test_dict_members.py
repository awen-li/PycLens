# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_dict_members

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = {'first': {'a': 1}, 'second': {'a': 1}, 'third': {'b': 2}}
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            data = plistlib.dumps(pl, fmt=fmt)
            pl2 = plistlib.loads(data)
            self.assertEqual(pl2, {'first': {'a': 1}, 'second': {'a': 1}, 'third': {'b': 2}})
            self.assertIsNot(pl2['first'], pl2['second'])
