# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_dumbdbm_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.init_db()
    with contextlib.closing(dumbdbm.open(_fname, 'r')) as f:
        self.read_helper(f)
        with self.assertRaisesRegex(dumbdbm.error, 'The database is opened for reading only'):
            f[b'g'] = b'x'
        with self.assertRaisesRegex(dumbdbm.error, 'The database is opened for reading only'):
            del f[b'a']
        self.assertEqual(f.get(b'a'), self._dict[b'a'])
        self.assertEqual(f.get(b'xxx', b'foo'), b'foo')
        self.assertIsNone(f.get(b'xxx'))
        with self.assertRaises(KeyError):
            f[b'xxx']
