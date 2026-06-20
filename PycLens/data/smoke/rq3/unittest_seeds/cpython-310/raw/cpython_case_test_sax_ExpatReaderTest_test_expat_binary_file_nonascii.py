# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_binary_file_nonascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fname = os_helper.TESTFN_UNICODE
    shutil.copyfile(TEST_XMLFILE, fname)
    self.addCleanup(os_helper.unlink, fname)
    parser = create_parser()
    result = BytesIO()
    xmlgen = XMLGenerator(result)
    parser.setContentHandler(xmlgen)
    parser.parse(open(fname, 'rb'))
    self.assertEqual(result.getvalue(), xml_test_out)
