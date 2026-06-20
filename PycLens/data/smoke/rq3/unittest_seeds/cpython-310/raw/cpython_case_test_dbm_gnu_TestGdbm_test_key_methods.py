# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_gnu.py
# case: TestGdbm_test_key_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.g = gdbm.open(filename, 'c')
    self.assertEqual(self.g.keys(), [])
    self.g['a'] = 'b'
    self.g['12345678910'] = '019237410982340912840198242'
    self.g[b'bytes'] = b'data'
    key_set = set(self.g.keys())
    self.assertEqual(key_set, set([b'a', b'bytes', b'12345678910']))
    self.assertIn('a', self.g)
    self.assertIn(b'a', self.g)
    self.assertEqual(self.g[b'bytes'], b'data')
    key = self.g.firstkey()
    while key:
        self.assertIn(key, key_set)
        key_set.remove(key)
        key = self.g.nextkey(key)
    self.assertEqual(self.g.get(b'a'), b'b')
    self.assertIsNone(self.g.get(b'xxx'))
    self.assertEqual(self.g.get(b'xxx', b'foo'), b'foo')
    with self.assertRaises(KeyError):
        self.g['xxx']
    self.assertEqual(self.g.setdefault(b'xxx', b'foo'), b'foo')
    self.assertEqual(self.g[b'xxx'], b'foo')
