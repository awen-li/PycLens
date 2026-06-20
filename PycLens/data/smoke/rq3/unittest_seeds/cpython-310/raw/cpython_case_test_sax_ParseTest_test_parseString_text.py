# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ParseTest_test_parseString_text

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = ('us-ascii', 'iso-8859-1', 'utf-8', 'utf-16', 'utf-16le', 'utf-16be')
    for encoding in encodings:
        self.check_parseString(xml_str(self.data, encoding))
    self.check_parseString(self.data)
