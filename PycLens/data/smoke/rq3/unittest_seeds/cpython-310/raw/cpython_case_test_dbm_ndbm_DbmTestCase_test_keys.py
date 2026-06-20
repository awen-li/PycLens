# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_ndbm.py
# case: DbmTestCase_test_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.d = dbm.ndbm.open(self.filename, 'c')
    self.assertEqual(self.d.keys(), [])
    self.d['a'] = 'b'
    self.d[b'bytes'] = b'data'
    self.d['12345678910'] = '019237410982340912840198242'
    self.d.keys()
    self.assertIn('a', self.d)
    self.assertIn(b'a', self.d)
    self.assertEqual(self.d[b'bytes'], b'data')
    self.assertEqual(self.d.get(b'a'), b'b')
    self.assertIsNone(self.d.get(b'xxx'))
    self.assertEqual(self.d.get(b'xxx', b'foo'), b'foo')
    with self.assertRaises(KeyError):
        self.d['xxx']
    self.assertEqual(self.d.setdefault(b'xxx', b'foo'), b'foo')
    self.assertEqual(self.d[b'xxx'], b'foo')
    self.d.close()
