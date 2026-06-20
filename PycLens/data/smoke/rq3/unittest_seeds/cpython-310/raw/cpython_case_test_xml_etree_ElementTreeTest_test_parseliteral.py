# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_parseliteral

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    element = ET.XML('<html><body>text</body></html>')
    self.assertEqual(ET.tostring(element, encoding='unicode'), '<html><body>text</body></html>')
    element = ET.fromstring('<html><body>text</body></html>')
    self.assertEqual(ET.tostring(element, encoding='unicode'), '<html><body>text</body></html>')
    sequence = ['<html><body>', 'text</bo', 'dy></html>']
    element = ET.fromstringlist(sequence)
    self.assertEqual(ET.tostring(element), b'<html><body>text</body></html>')
    self.assertEqual(b''.join(ET.tostringlist(element)), b'<html><body>text</body></html>')
    self.assertEqual(ET.tostring(element, 'ascii'), b"<?xml version='1.0' encoding='ascii'?>\n<html><body>text</body></html>")
    (_, ids) = ET.XMLID('<html><body>text</body></html>')
    self.assertEqual(len(ids), 0)
    (_, ids) = ET.XMLID("<html><body id='body'>text</body></html>")
    self.assertEqual(len(ids), 1)
    self.assertEqual(ids['body'].tag, 'body')
