# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_dumbdbm_modification

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.init_db()
    with contextlib.closing(dumbdbm.open(_fname, 'w')) as f:
        self._dict[b'g'] = f[b'g'] = b'indented'
        self.read_helper(f)
        self.assertEqual(f.setdefault(b'xxx', b'foo'), b'foo')
        self.assertEqual(f[b'xxx'], b'foo')
