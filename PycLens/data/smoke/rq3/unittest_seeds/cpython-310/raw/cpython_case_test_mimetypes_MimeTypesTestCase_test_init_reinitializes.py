# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_init_reinitializes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mimetypes.add_type('foo/bar', '.foobar')
    self.assertEqual(mimetypes.guess_extension('foo/bar'), '.foobar')
    mimetypes.init()
    self.assertEqual(mimetypes.guess_extension('foo/bar'), None)
