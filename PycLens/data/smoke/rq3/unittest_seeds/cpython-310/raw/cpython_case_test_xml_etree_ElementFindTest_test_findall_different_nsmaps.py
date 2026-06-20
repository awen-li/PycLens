# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementFindTest_test_findall_different_nsmaps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = ET.XML('\n            <a xmlns:x="X" xmlns:y="Y">\n                <x:b><c/></x:b>\n                <b/>\n                <c><x:b/><b/></c><y:b/>\n            </a>')
    nsmap = {'xx': 'X'}
    self.assertEqual(len(root.findall('.//xx:b', namespaces=nsmap)), 2)
    self.assertEqual(len(root.findall('.//b', namespaces=nsmap)), 2)
    nsmap = {'xx': 'Y'}
    self.assertEqual(len(root.findall('.//xx:b', namespaces=nsmap)), 1)
    self.assertEqual(len(root.findall('.//b', namespaces=nsmap)), 2)
    nsmap = {'xx': 'X', '': 'Y'}
    self.assertEqual(len(root.findall('.//xx:b', namespaces=nsmap)), 2)
    self.assertEqual(len(root.findall('.//b', namespaces=nsmap)), 1)
