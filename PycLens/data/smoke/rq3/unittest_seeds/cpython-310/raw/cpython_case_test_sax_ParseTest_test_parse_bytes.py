# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ParseTest_test_parse_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = ('us-ascii', 'utf-8', 'utf-16', 'utf-16le', 'utf-16be')
    for encoding in encodings:
        self.check_parse(BytesIO(xml_bytes(self.data, encoding)))
        make_xml_file(self.data, encoding)
        self.check_parse(TESTFN)
        with open(TESTFN, 'rb') as f:
            self.check_parse(f)
        self.check_parse(BytesIO(xml_bytes(self.data, encoding, None)))
        make_xml_file(self.data, encoding, None)
        self.check_parse(TESTFN)
        with open(TESTFN, 'rb') as f:
            self.check_parse(f)
    self.check_parse(BytesIO(xml_bytes(self.data, 'utf-8-sig', 'utf-8')))
    make_xml_file(self.data, 'utf-8-sig', 'utf-8')
    self.check_parse(TESTFN)
    with open(TESTFN, 'rb') as f:
        self.check_parse(f)
    self.check_parse(BytesIO(xml_bytes(self.data, 'utf-8-sig', None)))
    make_xml_file(self.data, 'utf-8-sig', None)
    self.check_parse(TESTFN)
    with open(TESTFN, 'rb') as f:
        self.check_parse(f)
    self.check_parse(BytesIO(xml_bytes(self.data, 'iso-8859-1')))
    make_xml_file(self.data, 'iso-8859-1')
    self.check_parse(TESTFN)
    with open(TESTFN, 'rb') as f:
        self.check_parse(f)
    with self.assertRaises(SAXException):
        self.check_parse(BytesIO(xml_bytes(self.data, 'iso-8859-1', None)))
    make_xml_file(self.data, 'iso-8859-1', None)
    with self.assertRaises(SAXException):
        self.check_parse(TESTFN)
    with open(TESTFN, 'rb') as f:
        with self.assertRaises(SAXException):
            self.check_parse(f)
