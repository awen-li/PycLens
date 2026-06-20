# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTypeTest_test_Element_subclass_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyElement(ET.Element):

        def __init__(self, tag, attrib={}, **extra):
            super(MyElement, self).__init__(tag + '__', attrib, **extra)
    mye = MyElement('foo', {'a': 1, 'b': 2}, c=3, d=4)
    self.assertEqual(mye.tag, 'foo__')
    self.assertEqual(sorted(mye.items()), [('a', 1), ('b', 2), ('c', 3), ('d', 4)])
