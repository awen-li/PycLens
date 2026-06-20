# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: WeirdMetadataTest_test_weird_metadata

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    info = self.t.info()
    self.assertEqual(len(info), 9)
    self.assertEqual(info['last-translator'], 'John Doe <jdoe@example.com>\nJane Foobar <jfoobar@example.com>')
