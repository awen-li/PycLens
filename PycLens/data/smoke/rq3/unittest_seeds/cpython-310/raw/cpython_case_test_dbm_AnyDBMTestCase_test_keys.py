# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm.py
# case: AnyDBMTestCase_test_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with dbm.open(_fname, 'c') as d:
        self.assertEqual(d.keys(), [])
        a = [(b'a', b'b'), (b'12345678910', b'019237410982340912840198242')]
        for (k, v) in a:
            d[k] = v
        self.assertEqual(sorted(d.keys()), sorted((k for (k, v) in a)))
        for (k, v) in a:
            self.assertIn(k, d)
            self.assertEqual(d[k], v)
        self.assertNotIn(b'xxx', d)
        self.assertRaises(KeyError, lambda : d[b'xxx'])
