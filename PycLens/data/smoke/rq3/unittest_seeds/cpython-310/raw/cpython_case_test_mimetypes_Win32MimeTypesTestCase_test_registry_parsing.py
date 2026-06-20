# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: Win32MimeTypesTestCase_test_registry_parsing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(self.db.guess_type('foo.txt'), ('text/plain', None))
    eq(self.db.guess_type('image.jpg'), ('image/jpeg', None))
    eq(self.db.guess_type('image.png'), ('image/png', None))
