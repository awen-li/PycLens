# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_inpsource_sysid_nonascii

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
    parser.parse(InputSource(fname))
    self.assertEqual(result.getvalue(), xml_test_out)
