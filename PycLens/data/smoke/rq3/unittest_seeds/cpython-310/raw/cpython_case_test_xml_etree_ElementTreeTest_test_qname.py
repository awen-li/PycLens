# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_qname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.Element('{uri}tag')
    self.serialize_check(elem, '<ns0:tag xmlns:ns0="uri" />')
    elem = ET.Element(ET.QName('{uri}tag'))
    self.serialize_check(elem, '<ns0:tag xmlns:ns0="uri" />')
    elem = ET.Element(ET.QName('uri', 'tag'))
    self.serialize_check(elem, '<ns0:tag xmlns:ns0="uri" />')
    elem = ET.Element(ET.QName('uri', 'tag'))
    subelem = ET.SubElement(elem, ET.QName('uri', 'tag1'))
    subelem = ET.SubElement(elem, ET.QName('uri', 'tag2'))
    self.serialize_check(elem, '<ns0:tag xmlns:ns0="uri"><ns0:tag1 /><ns0:tag2 /></ns0:tag>')
    elem.clear()
    elem.attrib['{uri}key'] = 'value'
    self.serialize_check(elem, '<ns0:tag xmlns:ns0="uri" ns0:key="value" />')
    elem.clear()
    elem.attrib[ET.QName('{uri}key')] = 'value'
    self.serialize_check(elem, '<ns0:tag xmlns:ns0="uri" ns0:key="value" />')
    elem.clear()
    elem.attrib['{uri}key'] = '{uri}value'
    self.serialize_check(elem, '<ns0:tag xmlns:ns0="uri" ns0:key="{uri}value" />')
    elem.clear()
    elem.attrib['{uri}key'] = ET.QName('{uri}value')
    self.serialize_check(elem, '<ns0:tag xmlns:ns0="uri" ns0:key="ns0:value" />')
    elem.clear()
    subelem = ET.Element('tag')
    subelem.attrib['{uri1}key'] = ET.QName('{uri2}value')
    elem.append(subelem)
    elem.append(subelem)
    self.serialize_check(elem, '<ns0:tag xmlns:ns0="uri" xmlns:ns1="uri1" xmlns:ns2="uri2"><tag ns1:key="ns2:value" /><tag ns1:key="ns2:value" /></ns0:tag>')
    self.assertEqual(str(ET.QName('ns', 'tag')), '{ns}tag')
    self.assertEqual(str(ET.QName('{ns}tag')), '{ns}tag')
    q1 = ET.QName('ns', 'tag')
    q2 = ET.QName('ns', 'tag')
    self.assertEqual(q1, q2)
    q2 = ET.QName('ns', 'other-tag')
    self.assertNotEqual(q1, q2)
    self.assertNotEqual(q1, 'ns:tag')
    self.assertEqual(q1, '{ns}tag')
