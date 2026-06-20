# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_inpsource_character_stream

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = create_parser()
    result = BytesIO()
    xmlgen = XMLGenerator(result)
    parser.setContentHandler(xmlgen)
    inpsrc = InputSource()
    with open(TEST_XMLFILE, 'rt', encoding='iso-8859-1') as f:
        inpsrc.setCharacterStream(f)
        parser.parse(inpsrc)
    self.assertEqual(result.getvalue(), xml_test_out)
