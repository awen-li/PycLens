# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_cdata

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.serialize_check(ET.XML('<tag>hello</tag>'), '<tag>hello</tag>')
    self.serialize_check(ET.XML('<tag>&#104;&#101;&#108;&#108;&#111;</tag>'), '<tag>hello</tag>')
    self.serialize_check(ET.XML('<tag><![CDATA[hello]]></tag>'), '<tag>hello</tag>')
