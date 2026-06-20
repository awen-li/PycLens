# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XIncludeTest_test_xinclude_repeated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from xml.etree import ElementInclude
    document = self.xinclude_loader('include_c1_repeated.xml')
    ElementInclude.include(document, self.xinclude_loader)
    self.assertEqual(1 + 4 * 2, len(document.findall('.//p')))
