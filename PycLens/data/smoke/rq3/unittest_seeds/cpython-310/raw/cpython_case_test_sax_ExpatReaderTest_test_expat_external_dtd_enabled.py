# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_external_dtd_enabled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(urllib.request.urlcleanup)
    parser = create_parser()
    parser.setFeature(feature_external_ges, True)
    resolver = self.TestEntityRecorder()
    parser.setEntityResolver(resolver)
    with self.assertRaises(URLError):
        parser.feed('<!DOCTYPE external SYSTEM "unsupported://non-existing">\n')
    self.assertEqual(resolver.entities, [(None, 'unsupported://non-existing')])
