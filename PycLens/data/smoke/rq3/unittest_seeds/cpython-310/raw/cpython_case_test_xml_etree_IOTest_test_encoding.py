# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.Element('tag')
    elem.text = 'abc'
    self.assertEqual(serialize(elem), '<tag>abc</tag>')
    for enc in ('utf-8', 'us-ascii'):
        with self.subTest(enc):
            self.assertEqual(serialize(elem, encoding=enc), b'<tag>abc</tag>')
            self.assertEqual(serialize(elem, encoding=enc.upper()), b'<tag>abc</tag>')
    for enc in ('iso-8859-1', 'utf-16', 'utf-32'):
        with self.subTest(enc):
            self.assertEqual(serialize(elem, encoding=enc), ("<?xml version='1.0' encoding='%s'?>\n<tag>abc</tag>" % enc).encode(enc))
            upper = enc.upper()
            self.assertEqual(serialize(elem, encoding=upper), ("<?xml version='1.0' encoding='%s'?>\n<tag>abc</tag>" % upper).encode(enc))
    elem = ET.Element('tag')
    elem.text = '<&"\'>'
    self.assertEqual(serialize(elem), '<tag>&lt;&amp;"\'&gt;</tag>')
    self.assertEqual(serialize(elem, encoding='utf-8'), b'<tag>&lt;&amp;"\'&gt;</tag>')
    self.assertEqual(serialize(elem, encoding='us-ascii'), b'<tag>&lt;&amp;"\'&gt;</tag>')
    for enc in ('iso-8859-1', 'utf-16', 'utf-32'):
        self.assertEqual(serialize(elem, encoding=enc), ('<?xml version=\'1.0\' encoding=\'%s\'?>\n<tag>&lt;&amp;"\'&gt;</tag>' % enc).encode(enc))
    elem = ET.Element('tag')
    elem.attrib['key'] = '<&"\'>'
    self.assertEqual(serialize(elem), '<tag key="&lt;&amp;&quot;\'&gt;" />')
    self.assertEqual(serialize(elem, encoding='utf-8'), b'<tag key="&lt;&amp;&quot;\'&gt;" />')
    self.assertEqual(serialize(elem, encoding='us-ascii'), b'<tag key="&lt;&amp;&quot;\'&gt;" />')
    for enc in ('iso-8859-1', 'utf-16', 'utf-32'):
        self.assertEqual(serialize(elem, encoding=enc), ('<?xml version=\'1.0\' encoding=\'%s\'?>\n<tag key="&lt;&amp;&quot;\'&gt;" />' % enc).encode(enc))
    elem = ET.Element('tag')
    elem.text = 'åöö<>'
    self.assertEqual(serialize(elem), '<tag>åöö&lt;&gt;</tag>')
    self.assertEqual(serialize(elem, encoding='utf-8'), b'<tag>\xc3\xa5\xc3\xb6\xc3\xb6&lt;&gt;</tag>')
    self.assertEqual(serialize(elem, encoding='us-ascii'), b'<tag>&#229;&#246;&#246;&lt;&gt;</tag>')
    for enc in ('iso-8859-1', 'utf-16', 'utf-32'):
        self.assertEqual(serialize(elem, encoding=enc), ("<?xml version='1.0' encoding='%s'?>\n<tag>åöö&lt;&gt;</tag>" % enc).encode(enc))
    elem = ET.Element('tag')
    elem.attrib['key'] = 'åöö<>'
    self.assertEqual(serialize(elem), '<tag key="åöö&lt;&gt;" />')
    self.assertEqual(serialize(elem, encoding='utf-8'), b'<tag key="\xc3\xa5\xc3\xb6\xc3\xb6&lt;&gt;" />')
    self.assertEqual(serialize(elem, encoding='us-ascii'), b'<tag key="&#229;&#246;&#246;&lt;&gt;" />')
    for enc in ('iso-8859-1', 'utf-16', 'utf-16le', 'utf-16be', 'utf-32'):
        self.assertEqual(serialize(elem, encoding=enc), ('<?xml version=\'1.0\' encoding=\'%s\'?>\n<tag key="åöö&lt;&gt;" />' % enc).encode(enc))
