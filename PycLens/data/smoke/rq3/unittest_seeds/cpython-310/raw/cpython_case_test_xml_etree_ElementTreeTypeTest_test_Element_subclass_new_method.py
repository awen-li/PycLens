# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTypeTest_test_Element_subclass_new_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyElement(ET.Element):

        def newmethod(self):
            return self.tag
    mye = MyElement('joe')
    self.assertEqual(mye.newmethod(), 'joe')
