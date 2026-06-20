# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_keysort_bytesio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = collections.OrderedDict()
    pl['b'] = 1
    pl['a'] = 2
    pl['c'] = 3
    for fmt in ALL_FORMATS:
        for sort_keys in (False, True):
            with self.subTest(fmt=fmt, sort_keys=sort_keys):
                b = BytesIO()
                plistlib.dump(pl, b, fmt=fmt, sort_keys=sort_keys)
                pl2 = plistlib.load(BytesIO(b.getvalue()), dict_type=collections.OrderedDict)
                self.assertEqual(dict(pl), dict(pl2))
                if sort_keys:
                    self.assertEqual(list(pl2.keys()), ['a', 'b', 'c'])
                else:
                    self.assertEqual(list(pl2.keys()), ['b', 'a', 'c'])
