# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ParseTest_test_parse_close_source

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    builtin_open = open
    fileobj = None

    def mock_open(*args):
        nonlocal fileobj
        fileobj = builtin_open(*args)
        return fileobj
    with mock.patch('xml.sax.saxutils.open', side_effect=mock_open):
        make_xml_file(self.data, 'iso-8859-1', None)
        with self.assertRaises(SAXException):
            self.check_parse(TESTFN)
        self.assertTrue(fileobj.closed)
