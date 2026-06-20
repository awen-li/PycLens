# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_keywords_args_api

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.guess_type(url='foo.html', strict=True), ('text/html', None))
    self.assertEqual(self.db.guess_all_extensions(type='image/jpg', strict=True), [])
    self.assertEqual(self.db.guess_extension(type='image/jpg', strict=False), '.jpg')
