# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_file_parsing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    sio = io.StringIO('x-application/x-unittest pyunit\n')
    self.db.readfp(sio)
    eq(self.db.guess_type('foo.pyunit'), ('x-application/x-unittest', None))
    eq(self.db.guess_extension('x-application/x-unittest'), '.pyunit')
