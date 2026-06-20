# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm.py
# case: AnyDBMTestCase_test_anydbm_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.init_db()
    f = dbm.open(_fname, 'r')
    self.read_helper(f)
    self.assertEqual(f.get(b'a'), self._dict['a'])
    self.assertEqual(f.get(b'xxx', b'foo'), b'foo')
    self.assertIsNone(f.get(b'xxx'))
    with self.assertRaises(KeyError):
        f[b'xxx']
    f.close()
