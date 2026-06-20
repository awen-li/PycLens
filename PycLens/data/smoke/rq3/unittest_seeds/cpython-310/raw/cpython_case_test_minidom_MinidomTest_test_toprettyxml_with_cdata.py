# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_minidom.py
# case: MinidomTest_test_toprettyxml_with_cdata

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xml_str = '<?xml version="1.0" ?><root><node><![CDATA[</data>]]></node></root>'
    doc = parseString(xml_str)
    self.assertEqual(doc.toprettyxml(), '<?xml version="1.0" ?>\n<root>\n\t<node><![CDATA[</data>]]></node>\n</root>\n')
