# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_attrib

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.Element('tag')
    elem.get('key')
    self.assertEqual(elem.get('key', 'default'), 'default')
    elem.set('key', 'value')
    self.assertEqual(elem.get('key'), 'value')
    elem = ET.Element('tag', key='value')
    self.assertEqual(elem.get('key'), 'value')
    self.assertEqual(elem.attrib, {'key': 'value'})
    attrib = {'key': 'value'}
    elem = ET.Element('tag', attrib)
    attrib.clear()
    self.assertEqual(elem.get('key'), 'value')
    self.assertEqual(elem.attrib, {'key': 'value'})
    attrib = {'key': 'value'}
    elem = ET.Element('tag', **attrib)
    attrib.clear()
    self.assertEqual(elem.get('key'), 'value')
    self.assertEqual(elem.attrib, {'key': 'value'})
    elem = ET.Element('tag', {'key': 'other'}, key='value')
    self.assertEqual(elem.get('key'), 'value')
    self.assertEqual(elem.attrib, {'key': 'value'})
    elem = ET.Element('test')
    elem.text = 'aa'
    elem.set('testa', 'testval')
    elem.set('testb', 'test2')
    self.assertEqual(ET.tostring(elem), b'<test testa="testval" testb="test2">aa</test>')
    self.assertEqual(sorted(elem.keys()), ['testa', 'testb'])
    self.assertEqual(sorted(elem.items()), [('testa', 'testval'), ('testb', 'test2')])
    self.assertEqual(elem.attrib['testb'], 'test2')
    elem.attrib['testb'] = 'test1'
    elem.attrib['testc'] = 'test2'
    self.assertEqual(ET.tostring(elem), b'<test testa="testval" testb="test1" testc="test2">aa</test>')
    elem = ET.Element('test')
    elem.set('a', '\r')
    elem.set('b', '\r\n')
    elem.set('c', '\t\n\r ')
    elem.set('d', '\n\n\r\r\t\t  ')
    self.assertEqual(ET.tostring(elem), b'<test a="&#13;" b="&#13;&#10;" c="&#09;&#10;&#13; " d="&#10;&#10;&#13;&#13;&#09;&#09;  " />')
