# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_locator_withinfo_nonascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fname = os_helper.TESTFN_UNICODE
    shutil.copyfile(TEST_XMLFILE, fname)
    self.addCleanup(os_helper.unlink, fname)
    result = BytesIO()
    xmlgen = XMLGenerator(result)
    parser = create_parser()
    parser.setContentHandler(xmlgen)
    parser.parse(fname)
    self.assertEqual(parser.getSystemId(), fname)
    self.assertEqual(parser.getPublicId(), None)
