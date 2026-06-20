# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_makeelement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.Element('tag')
    attrib = {'key': 'value'}
    subelem = elem.makeelement('subtag', attrib)
    self.assertIsNot(subelem.attrib, attrib, msg='attrib aliasing')
    elem.append(subelem)
    self.serialize_check(elem, '<tag><subtag key="value" /></tag>')
    elem.clear()
    self.serialize_check(elem, '<tag />')
    elem.append(subelem)
    self.serialize_check(elem, '<tag><subtag key="value" /></tag>')
    elem.extend([subelem, subelem])
    self.serialize_check(elem, '<tag><subtag key="value" /><subtag key="value" /><subtag key="value" /></tag>')
    elem[:] = [subelem]
    self.serialize_check(elem, '<tag><subtag key="value" /></tag>')
    elem[:] = tuple([subelem])
    self.serialize_check(elem, '<tag><subtag key="value" /></tag>')
