# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_element_factory_pure_python_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = ET._Element_Py
    self.assertEqual(base.__module__, 'xml.etree.ElementTree')

    class MyElement(base, ValueError):
        pass
    self._check_element_factory_class(MyElement)
