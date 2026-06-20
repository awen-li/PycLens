# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimetypesCliTestCase_test_guess_extension

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    extension = self.mimetypes_cmd('-l', '-e', 'image/jpg')
    eq(extension, '.jpg')
    extension = self.mimetypes_cmd('-e', 'image/jpg')
    eq(extension, "I don't know anything about type image/jpg")
    extension = self.mimetypes_cmd('-e', 'image/jpeg')
    eq(extension, '.jpg')
