# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_data_urls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    guess_type = self.db.guess_type
    eq(guess_type('data:invalidDataWithoutComma'), (None, None))
    eq(guess_type('data:,thisIsTextPlain'), ('text/plain', None))
    eq(guess_type('data:;base64,thisIsTextPlain'), ('text/plain', None))
    eq(guess_type('data:text/x-foo,thisIsTextXFoo'), ('text/x-foo', None))
