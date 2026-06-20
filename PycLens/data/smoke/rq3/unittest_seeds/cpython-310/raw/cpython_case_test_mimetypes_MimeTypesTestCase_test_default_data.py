# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_default_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(self.db.guess_type('foo.html'), ('text/html', None))
    eq(self.db.guess_type('foo.HTML'), ('text/html', None))
    eq(self.db.guess_type('foo.tgz'), ('application/x-tar', 'gzip'))
    eq(self.db.guess_type('foo.tar.gz'), ('application/x-tar', 'gzip'))
    eq(self.db.guess_type('foo.tar.Z'), ('application/x-tar', 'compress'))
    eq(self.db.guess_type('foo.tar.bz2'), ('application/x-tar', 'bzip2'))
    eq(self.db.guess_type('foo.tar.xz'), ('application/x-tar', 'xz'))
