# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ParseTest_test_parse_text

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = ('us-ascii', 'iso-8859-1', 'utf-8', 'utf-16', 'utf-16le', 'utf-16be')
    for encoding in encodings:
        self.check_parse(StringIO(xml_str(self.data, encoding)))
        make_xml_file(self.data, encoding)
        with open(TESTFN, 'r', encoding=encoding) as f:
            self.check_parse(f)
        self.check_parse(StringIO(self.data))
        make_xml_file(self.data, encoding, None)
        with open(TESTFN, 'r', encoding=encoding) as f:
            self.check_parse(f)
