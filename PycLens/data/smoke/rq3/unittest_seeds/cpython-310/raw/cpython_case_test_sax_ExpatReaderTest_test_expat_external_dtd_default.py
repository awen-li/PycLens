# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_external_dtd_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = create_parser()
    resolver = self.TestEntityRecorder()
    parser.setEntityResolver(resolver)
    parser.feed('<!DOCTYPE external SYSTEM "unsupported://non-existing">\n')
    parser.feed('<doc />')
    parser.close()
    self.assertEqual(resolver.entities, [])
