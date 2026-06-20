# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_indent_level

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<html><body><p>pre<br/>post</p><p>text</p></body></html>')
    with self.assertRaises(ValueError):
        ET.indent(elem, level=-1)
    self.assertEqual(ET.tostring(elem), b'<html><body><p>pre<br />post</p><p>text</p></body></html>')
    ET.indent(elem, level=2)
    self.assertEqual(ET.tostring(elem), b'<html>\n      <body>\n        <p>pre<br />post</p>\n        <p>text</p>\n      </body>\n    </html>')
    elem = ET.XML('<html><body><p>pre<br/>post</p><p>text</p></body></html>')
    ET.indent(elem, level=1, space=' ')
    self.assertEqual(ET.tostring(elem), b'<html>\n  <body>\n   <p>pre<br />post</p>\n   <p>text</p>\n  </body>\n </html>')
