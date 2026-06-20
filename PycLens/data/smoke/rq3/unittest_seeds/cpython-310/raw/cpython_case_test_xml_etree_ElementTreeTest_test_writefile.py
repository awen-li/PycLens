# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_writefile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.Element('tag')
    elem.text = 'text'
    self.serialize_check(elem, '<tag>text</tag>')
    ET.SubElement(elem, 'subtag').text = 'subtext'
    self.serialize_check(elem, '<tag>text<subtag>subtext</subtag></tag>')
    elem.tag = None
    self.serialize_check(elem, 'text<subtag>subtext</subtag>')
    elem.insert(0, ET.Comment('comment'))
    self.serialize_check(elem, 'text<!--comment--><subtag>subtext</subtag>')
    elem[0] = ET.PI('key', 'value')
    self.serialize_check(elem, 'text<?key value?><subtag>subtext</subtag>')
