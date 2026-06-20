# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_indent_space_caching

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<html><body><p>par</p><p>text</p><p><br/></p><p /></body></html>')
    ET.indent(elem)
    self.assertEqual({el.tail for el in elem.iter()}, {None, '\n', '\n  ', '\n    '})
    self.assertEqual({el.text for el in elem.iter()}, {None, '\n  ', '\n    ', '\n      ', 'par', 'text'})
    self.assertEqual(len({el.tail for el in elem.iter()}), len({id(el.tail) for el in elem.iter()}))
