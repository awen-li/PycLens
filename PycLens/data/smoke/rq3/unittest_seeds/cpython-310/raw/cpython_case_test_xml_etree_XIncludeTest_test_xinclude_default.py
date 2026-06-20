# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XIncludeTest_test_xinclude_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from xml.etree import ElementInclude
    doc = self.xinclude_loader('default.xml')
    ElementInclude.include(doc, self._my_loader)
    self.assertEqual(serialize(doc), '<document>\n  <p>Example.</p>\n  <root>\n   <element key="value">text</element>\n   <element>text</element>tail\n   <empty-element />\n</root>\n</document>')
