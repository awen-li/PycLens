# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_ndbm.py
# case: DbmTestCase_test_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with dbm.ndbm.open(self.filename, 'c') as db:
        db['Unicode key 🐍'] = 'Unicode value 🐍'
    with dbm.ndbm.open(self.filename, 'r') as db:
        self.assertEqual(list(db.keys()), ['Unicode key 🐍'.encode()])
        self.assertTrue('Unicode key 🐍'.encode() in db)
        self.assertTrue('Unicode key 🐍' in db)
        self.assertEqual(db['Unicode key 🐍'.encode()], 'Unicode value 🐍'.encode())
        self.assertEqual(db['Unicode key 🐍'], 'Unicode value 🐍'.encode())
