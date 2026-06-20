# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_html_empty_elems_serialization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for element in ['AREA', 'BASE', 'BASEFONT', 'BR', 'COL', 'FRAME', 'HR', 'IMG', 'INPUT', 'ISINDEX', 'LINK', 'META', 'PARAM']:
        for elem in [element, element.lower()]:
            expected = '<%s>' % elem
            serialized = serialize(ET.XML('<%s />' % elem), method='html')
            self.assertEqual(serialized, expected)
            serialized = serialize(ET.XML('<%s></%s>' % (elem, elem)), method='html')
            self.assertEqual(serialized, expected)
