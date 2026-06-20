# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: MiscTests_test_setstate_leaks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = cET.Element.__new__(cET.Element)
    for i in range(100):
        elem.__setstate__({'tag': 'foo', 'attrib': {'bar': 42}, '_children': [cET.Element('child')], 'text': 'text goes here', 'tail': 'opposite of head'})
    self.assertEqual(elem.tag, 'foo')
    self.assertEqual(elem.text, 'text goes here')
    self.assertEqual(elem.tail, 'opposite of head')
    self.assertEqual(list(elem.attrib.items()), [('bar', 42)])
    self.assertEqual(len(elem), 1)
    self.assertEqual(elem[0].tag, 'child')
