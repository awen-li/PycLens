# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm.py
# case: AnyDBMTestCase_test_anydbm_modification

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.init_db()
    f = dbm.open(_fname, 'c')
    self._dict['g'] = f[b'g'] = b'indented'
    self.read_helper(f)
    self.assertEqual(f.setdefault(b'xxx', b'foo'), b'foo')
    self.assertEqual(f[b'xxx'], b'foo')
    f.close()
