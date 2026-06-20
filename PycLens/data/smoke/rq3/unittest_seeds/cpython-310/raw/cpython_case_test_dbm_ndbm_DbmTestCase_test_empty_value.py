# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_ndbm.py
# case: DbmTestCase_test_empty_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if dbm.ndbm.library == 'Berkeley DB':
        self.skipTest("Berkeley DB doesn't distinguish the empty value from the absent one")
    self.d = dbm.ndbm.open(self.filename, 'c')
    self.assertEqual(self.d.keys(), [])
    self.d['empty'] = ''
    self.assertEqual(self.d.keys(), [b'empty'])
    self.assertIn(b'empty', self.d)
    self.assertEqual(self.d[b'empty'], b'')
    self.assertEqual(self.d.get(b'empty'), b'')
    self.assertEqual(self.d.setdefault(b'empty'), b'')
    self.d.close()
