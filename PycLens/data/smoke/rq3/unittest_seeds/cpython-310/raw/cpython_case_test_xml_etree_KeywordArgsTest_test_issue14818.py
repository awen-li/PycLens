# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: KeywordArgsTest_test_issue14818

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ET.XML('<a>foo</a>')
    self.assertEqual(x.find('a', None), x.find(path='a', namespaces=None))
    self.assertEqual(x.findtext('a', None, None), x.findtext(path='a', default=None, namespaces=None))
    self.assertEqual(x.findall('a', None), x.findall(path='a', namespaces=None))
    self.assertEqual(list(x.iterfind('a', None)), list(x.iterfind(path='a', namespaces=None)))
    self.assertEqual(ET.Element('a').attrib, {})
    elements = [ET.Element('a', dict(href='#', id='foo')), ET.Element('a', attrib=dict(href='#', id='foo')), ET.Element('a', dict(href='#'), id='foo'), ET.Element('a', href='#', id='foo'), ET.Element('a', dict(href='#', id='foo'), href='#', id='foo')]
    for e in elements:
        self.assertEqual(e.tag, 'a')
        self.assertEqual(e.attrib, dict(href='#', id='foo'))
    e2 = ET.SubElement(elements[0], 'foobar', attrib={'key1': 'value1'})
    self.assertEqual(e2.attrib['key1'], 'value1')
    with self.assertRaisesRegex(TypeError, 'must be dict, not str'):
        ET.Element('a', "I'm not a dict")
    with self.assertRaisesRegex(TypeError, 'must be dict, not str'):
        ET.Element('a', attrib="I'm not a dict")
