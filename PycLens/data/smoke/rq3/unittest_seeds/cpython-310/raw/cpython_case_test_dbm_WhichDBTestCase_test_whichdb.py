# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm.py
# case: WhichDBTestCase_test_whichdb

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(setattr, dbm, '_defaultmod', dbm._defaultmod)
    for module in dbm_iterator():
        name = module.__name__
        setup_test_dir()
        dbm._defaultmod = module
        with module.open(_fname, 'c'):
            pass
        self.assertEqual(name, self.dbm.whichdb(_fname))
        with module.open(_fname, 'w') as f:
            f[b'1'] = b'1'
            self.assertIn(b'1', f)
            self.assertEqual(f[b'1'], b'1')
        self.assertEqual(name, self.dbm.whichdb(_fname))
