# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTypeTest_test_Element_subclass_find

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyElement(ET.Element):
        pass
    e = ET.Element('foo')
    e.text = 'text'
    sub = MyElement('bar')
    sub.text = 'subtext'
    e.append(sub)
    self.assertEqual(e.findtext('bar'), 'subtext')
    self.assertEqual(e.find('bar').tag, 'bar')
    found = list(e.findall('bar'))
    self.assertEqual(len(found), 1, found)
    self.assertEqual(found[0].tag, 'bar')
