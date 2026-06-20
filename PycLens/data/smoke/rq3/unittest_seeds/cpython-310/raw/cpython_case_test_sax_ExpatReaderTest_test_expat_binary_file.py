# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_binary_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = create_parser()
    result = BytesIO()
    xmlgen = XMLGenerator(result)
    parser.setContentHandler(xmlgen)
    with open(TEST_XMLFILE, 'rb') as f:
        parser.parse(f)
    self.assertEqual(result.getvalue(), xml_test_out)
