# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_minidom.py
# case: MinidomTest_test_cdata_parsing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xml_str = '<?xml version="1.0" ?><root><node><![CDATA[</data>]]></node></root>'
    dom1 = parseString(xml_str)
    self.checkWholeText(dom1.getElementsByTagName('node')[0].firstChild, '</data>')
    dom2 = parseString(dom1.toprettyxml())
    self.checkWholeText(dom2.getElementsByTagName('node')[0].firstChild, '</data>')
