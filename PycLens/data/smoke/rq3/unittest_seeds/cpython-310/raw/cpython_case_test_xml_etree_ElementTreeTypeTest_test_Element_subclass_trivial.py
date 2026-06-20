# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTypeTest_test_Element_subclass_trivial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyElement(ET.Element):
        pass
    mye = MyElement('foo')
    self.assertIsInstance(mye, ET.Element)
    self.assertIsInstance(mye, MyElement)
    self.assertEqual(mye.tag, 'foo')
    mye.text = 'joe'
    self.assertEqual(mye.text, 'joe')
