# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_xmltoolkit39

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ET.XML(b"<?xml version='1.0' encoding='iso-8859-1'?><t\xe4g />")
    self.assertEqual(ET.tostring(tree, 'utf-8'), b'<t\xc3\xa4g />')
    tree = ET.XML(b"<?xml version='1.0' encoding='iso-8859-1'?><tag \xe4ttr='v&#228;lue' />")
    self.assertEqual(tree.attrib, {'ättr': 'välue'})
    self.assertEqual(ET.tostring(tree, 'utf-8'), b'<tag \xc3\xa4ttr="v\xc3\xa4lue" />')
    tree = ET.XML(b"<?xml version='1.0' encoding='iso-8859-1'?><t\xe4g>text</t\xe4g>")
    self.assertEqual(ET.tostring(tree, 'utf-8'), b'<t\xc3\xa4g>text</t\xc3\xa4g>')
    tree = ET.Element('täg')
    self.assertEqual(ET.tostring(tree, 'utf-8'), b'<t\xc3\xa4g />')
    tree = ET.Element('tag')
    tree.set('ättr', 'välue')
    self.assertEqual(ET.tostring(tree, 'utf-8'), b'<tag \xc3\xa4ttr="v\xc3\xa4lue" />')
