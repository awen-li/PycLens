# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLParserTest_test_doctype_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings():
        warnings.simplefilter('error', DeprecationWarning)
        parser = ET.XMLParser()
        parser.feed(self.sample2)
        parser.close()
