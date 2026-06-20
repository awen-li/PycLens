# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_filename_with_url_delimiters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    gzip_expected = ('application/x-tar', 'gzip')
    eq(self.db.guess_type(';1.tar.gz'), gzip_expected)
    eq(self.db.guess_type('?1.tar.gz'), gzip_expected)
    eq(self.db.guess_type('#1.tar.gz'), gzip_expected)
    eq(self.db.guess_type('#1#.tar.gz'), gzip_expected)
    eq(self.db.guess_type(';1#.tar.gz'), gzip_expected)
    eq(self.db.guess_type(';&1=123;?.tar.gz'), gzip_expected)
    eq(self.db.guess_type('?k1=v1&k2=v2.tar.gz'), gzip_expected)
    eq(self.db.guess_type(' \\"\\`;b&b&c |.tar.gz'), gzip_expected)
