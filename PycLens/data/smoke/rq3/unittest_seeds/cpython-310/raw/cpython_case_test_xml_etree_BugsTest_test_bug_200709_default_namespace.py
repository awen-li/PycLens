# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_200709_default_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.Element('{default}elem')
    s = ET.SubElement(e, '{default}elem')
    self.assertEqual(serialize(e, default_namespace='default'), '<elem xmlns="default"><elem /></elem>')
    e = ET.Element('{default}elem')
    s = ET.SubElement(e, '{default}elem')
    s = ET.SubElement(e, '{not-default}elem')
    self.assertEqual(serialize(e, default_namespace='default'), '<elem xmlns="default" xmlns:ns1="not-default"><elem /><ns1:elem /></elem>')
    e = ET.Element('{default}elem')
    s = ET.SubElement(e, '{default}elem')
    s = ET.SubElement(e, 'elem')
    with self.assertRaises(ValueError) as cm:
        serialize(e, default_namespace='default')
    self.assertEqual(str(cm.exception), 'cannot use non-qualified names with default_namespace option')
