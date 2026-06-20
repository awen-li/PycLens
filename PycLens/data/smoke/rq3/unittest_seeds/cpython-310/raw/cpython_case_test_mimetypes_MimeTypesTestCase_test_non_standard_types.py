# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_non_standard_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(self.db.guess_type('foo.xul', strict=True), (None, None))
    eq(self.db.guess_extension('image/jpg', strict=True), None)
    eq(self.db.guess_type('foo.xul', strict=False), ('text/xul', None))
    eq(self.db.guess_type('foo.XUL', strict=False), ('text/xul', None))
    eq(self.db.guess_type('foo.invalid', strict=False), (None, None))
    eq(self.db.guess_extension('image/jpg', strict=False), '.jpg')
    eq(self.db.guess_extension('image/JPG', strict=False), '.jpg')
