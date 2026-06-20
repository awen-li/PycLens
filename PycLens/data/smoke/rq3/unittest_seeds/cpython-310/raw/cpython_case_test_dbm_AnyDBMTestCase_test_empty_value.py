# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm.py
# case: AnyDBMTestCase_test_empty_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if getattr(dbm._defaultmod, 'library', None) == 'Berkeley DB':
        self.skipTest("Berkeley DB doesn't distinguish the empty value from the absent one")
    f = dbm.open(_fname, 'c')
    self.assertEqual(f.keys(), [])
    f[b'empty'] = b''
    self.assertEqual(f.keys(), [b'empty'])
    self.assertIn(b'empty', f)
    self.assertEqual(f[b'empty'], b'')
    self.assertEqual(f.get(b'empty'), b'')
    self.assertEqual(f.setdefault(b'empty'), b'')
    f.close()
