# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    getpreferredencoding = locale.getpreferredencoding
    self.addCleanup(setattr, locale, 'getpreferredencoding', getpreferredencoding)
    locale.getpreferredencoding = lambda : 'ascii'
    filename = support.findfile('mime.types')
    mimes = mimetypes.MimeTypes([filename])
    exts = mimes.guess_all_extensions('application/vnd.geocube+xml', strict=True)
    self.assertEqual(exts, ['.g3', '.g³'])
