# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_xmltoolkit21

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(elem):
        with self.assertRaises(TypeError) as cm:
            serialize(elem)
        self.assertEqual(str(cm.exception), 'cannot serialize 123 (type int)')
    elem = ET.Element(123)
    check(elem)
    elem = ET.Element('elem')
    elem.text = 123
    check(elem)
    elem = ET.Element('elem')
    elem.tail = 123
    check(elem)
    elem = ET.Element('elem')
    elem.set(123, '123')
    check(elem)
    elem = ET.Element('elem')
    elem.set('123', 123)
    check(elem)
