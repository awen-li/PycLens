# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_indent_space

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<html><body><p>pre<br/>post</p><p>text</p></body></html>')
    ET.indent(elem, space='\t')
    self.assertEqual(ET.tostring(elem), b'<html>\n\t<body>\n\t\t<p>pre<br />post</p>\n\t\t<p>text</p>\n\t</body>\n</html>')
    elem = ET.XML('<html><body><p>pre<br/>post</p><p>text</p></body></html>')
    ET.indent(elem, space='')
    self.assertEqual(ET.tostring(elem), b'<html>\n<body>\n<p>pre<br />post</p>\n<p>text</p>\n</body>\n</html>')
