# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ParseTest_test_parseString_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = ('us-ascii', 'utf-8', 'utf-16', 'utf-16le', 'utf-16be')
    for encoding in encodings:
        self.check_parseString(xml_bytes(self.data, encoding))
        self.check_parseString(xml_bytes(self.data, encoding, None))
    self.check_parseString(xml_bytes(self.data, 'utf-8-sig', 'utf-8'))
    self.check_parseString(xml_bytes(self.data, 'utf-8-sig', None))
    self.check_parseString(xml_bytes(self.data, 'iso-8859-1'))
    with self.assertRaises(SAXException):
        self.check_parseString(xml_bytes(self.data, 'iso-8859-1', None))
