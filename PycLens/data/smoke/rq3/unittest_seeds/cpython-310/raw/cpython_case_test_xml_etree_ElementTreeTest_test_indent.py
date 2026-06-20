# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_indent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<root></root>')
    ET.indent(elem)
    self.assertEqual(ET.tostring(elem), b'<root />')
    elem = ET.XML('<html><body>text</body></html>')
    ET.indent(elem)
    self.assertEqual(ET.tostring(elem), b'<html>\n  <body>text</body>\n</html>')
    elem = ET.XML('<html> <body>text</body>  </html>')
    ET.indent(elem)
    self.assertEqual(ET.tostring(elem), b'<html>\n  <body>text</body>\n</html>')
    elem = ET.XML('<html><body>text</body>tail</html>')
    ET.indent(elem)
    self.assertEqual(ET.tostring(elem), b'<html>\n  <body>text</body>tail</html>')
    elem = ET.XML('<html><body><p>par</p>\n<p>text</p>\t<p><br/></p></body></html>')
    ET.indent(elem)
    self.assertEqual(ET.tostring(elem), b'<html>\n  <body>\n    <p>par</p>\n    <p>text</p>\n    <p>\n      <br />\n    </p>\n  </body>\n</html>')
    elem = ET.XML('<html><body><p>pre<br/>post</p><p>text</p></body></html>')
    ET.indent(elem)
    self.assertEqual(ET.tostring(elem), b'<html>\n  <body>\n    <p>pre<br />post</p>\n    <p>text</p>\n  </body>\n</html>')
