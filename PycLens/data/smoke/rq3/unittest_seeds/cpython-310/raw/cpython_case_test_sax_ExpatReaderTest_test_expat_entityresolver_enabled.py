# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_entityresolver_enabled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = create_parser()
    parser.setFeature(feature_external_ges, True)
    parser.setEntityResolver(self.TestEntityResolver())
    result = BytesIO()
    parser.setContentHandler(XMLGenerator(result))
    parser.feed('<!DOCTYPE doc [\n')
    parser.feed('  <!ENTITY test SYSTEM "whatever">\n')
    parser.feed(']>\n')
    parser.feed('<doc>&test;</doc>')
    parser.close()
    self.assertEqual(result.getvalue(), start + b'<doc><entity></entity></doc>')
