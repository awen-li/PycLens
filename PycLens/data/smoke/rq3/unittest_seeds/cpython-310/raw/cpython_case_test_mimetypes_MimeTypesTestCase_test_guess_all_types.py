# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_guess_all_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    all = self.db.guess_all_extensions('text/plain', strict=True)
    self.assertTrue(set(all) >= {'.bat', '.c', '.h', '.ksh', '.pl', '.txt'})
    self.assertEqual(len(set(all)), len(all))
    all = self.db.guess_all_extensions('image/jpg', strict=False)
    self.assertEqual(all, ['.jpg'])
    all = self.db.guess_all_extensions('image/jpg', strict=True)
    self.assertEqual(all, [])
    self.db.add_type('test-type', '.strict-ext')
    self.db.add_type('test-type', '.non-strict-ext', strict=False)
    all = self.db.guess_all_extensions('test-type', strict=False)
    self.assertEqual(all, ['.strict-ext', '.non-strict-ext'])
    all = self.db.guess_all_extensions('test-type')
    self.assertEqual(all, ['.strict-ext'])
    all.append('.no-such-ext')
    all = self.db.guess_all_extensions('test-type')
    self.assertNotIn('.no-such-ext', all)
