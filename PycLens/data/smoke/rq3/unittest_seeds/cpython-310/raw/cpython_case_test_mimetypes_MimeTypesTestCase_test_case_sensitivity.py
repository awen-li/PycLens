# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_case_sensitivity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(self.db.guess_type('foobar.HTML'), self.db.guess_type('foobar.html'))
    eq(self.db.guess_type('foobar.TGZ'), self.db.guess_type('foobar.tgz'))
    eq(self.db.guess_type('foobar.tar.Z'), ('application/x-tar', 'compress'))
    eq(self.db.guess_type('foobar.tar.z'), (None, None))
