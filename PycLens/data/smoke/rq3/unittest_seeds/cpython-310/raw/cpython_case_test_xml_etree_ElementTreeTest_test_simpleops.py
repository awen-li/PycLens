# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_simpleops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<body><tag/></body>')
    self.serialize_check(elem, '<body><tag /></body>')
    e = ET.Element('tag2')
    elem.append(e)
    self.serialize_check(elem, '<body><tag /><tag2 /></body>')
    elem.remove(e)
    self.serialize_check(elem, '<body><tag /></body>')
    elem.insert(0, e)
    self.serialize_check(elem, '<body><tag2 /><tag /></body>')
    elem.remove(e)
    elem.extend([e])
    self.serialize_check(elem, '<body><tag /><tag2 /></body>')
    elem.remove(e)
    elem.extend(iter([e]))
    self.serialize_check(elem, '<body><tag /><tag2 /></body>')
    elem.remove(e)
    element = ET.Element('tag', key='value')
    self.serialize_check(element, '<tag key="value" />')
    subelement = ET.Element('subtag')
    element.append(subelement)
    self.serialize_check(element, '<tag key="value"><subtag /></tag>')
    element.insert(0, subelement)
    self.serialize_check(element, '<tag key="value"><subtag /><subtag /></tag>')
    element.remove(subelement)
    self.serialize_check(element, '<tag key="value"><subtag /></tag>')
    element.remove(subelement)
    self.serialize_check(element, '<tag key="value" />')
    with self.assertRaises(ValueError) as cm:
        element.remove(subelement)
    self.assertEqual(str(cm.exception), 'list.remove(x): x not in list')
    self.serialize_check(element, '<tag key="value" />')
    element[0:0] = [subelement, subelement, subelement]
    self.serialize_check(element[1], '<subtag />')
    self.assertEqual(element[1:9], [element[1], element[2]])
    self.assertEqual(element[:9:2], [element[0], element[2]])
    del element[1:2]
    self.serialize_check(element, '<tag key="value"><subtag /><subtag /></tag>')
