# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XIncludeTest_test_xinclude_failures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from xml.etree import ElementInclude
    document = ET.XML(XINCLUDE['C1.xml'])
    with self.assertRaises(ElementInclude.FatalIncludeError) as cm:
        ElementInclude.include(document, loader=self.none_loader)
    self.assertEqual(str(cm.exception), "cannot load 'disclaimer.xml' as 'xml'")
    document = ET.XML(XINCLUDE['C2.xml'])
    with self.assertRaises(ElementInclude.FatalIncludeError) as cm:
        ElementInclude.include(document, loader=self.none_loader)
    self.assertEqual(str(cm.exception), "cannot load 'count.txt' as 'text'")
    document = ET.XML(XINCLUDE_BAD['B1.xml'])
    with self.assertRaises(ElementInclude.FatalIncludeError) as cm:
        ElementInclude.include(document, loader=self.none_loader)
    self.assertEqual(str(cm.exception), "unknown parse type in xi:include tag ('BAD_TYPE')")
    document = ET.XML(XINCLUDE_BAD['B2.xml'])
    with self.assertRaises(ElementInclude.FatalIncludeError) as cm:
        ElementInclude.include(document, loader=self.none_loader)
    self.assertEqual(str(cm.exception), "xi:fallback tag must be child of xi:include ('{http://www.w3.org/2001/XInclude}fallback')")
    document = self.xinclude_loader('Recursive1.xml')
    with self.assertRaises(ElementInclude.FatalIncludeError) as cm:
        ElementInclude.include(document, self.xinclude_loader)
    self.assertEqual(str(cm.exception), 'recursive include of Recursive2.xml')
    document = self.xinclude_loader('Recursive1.xml')
    with self.assertRaises(ElementInclude.FatalIncludeError) as cm:
        ElementInclude.include(document, self.xinclude_loader, max_depth=None)
    self.assertEqual(str(cm.exception), 'recursive include of Recursive2.xml')
    document = self.xinclude_loader('Recursive1.xml')
    with self.assertRaises(ElementInclude.LimitedRecursiveIncludeError) as cm:
        ElementInclude.include(document, self.xinclude_loader, max_depth=0)
    self.assertEqual(str(cm.exception), 'maximum xinclude depth reached when including file Recursive2.xml')
    document = self.xinclude_loader('Recursive1.xml')
    with self.assertRaises(ElementInclude.LimitedRecursiveIncludeError) as cm:
        ElementInclude.include(document, self.xinclude_loader, max_depth=1)
    self.assertEqual(str(cm.exception), 'maximum xinclude depth reached when including file Recursive3.xml')
    document = self.xinclude_loader('Recursive1.xml')
    with self.assertRaises(ElementInclude.LimitedRecursiveIncludeError) as cm:
        ElementInclude.include(document, self.xinclude_loader, max_depth=2)
    self.assertEqual(str(cm.exception), 'maximum xinclude depth reached when including file Recursive1.xml')
    document = self.xinclude_loader('Recursive1.xml')
    with self.assertRaises(ElementInclude.FatalIncludeError) as cm:
        ElementInclude.include(document, self.xinclude_loader, max_depth=3)
    self.assertEqual(str(cm.exception), 'recursive include of Recursive2.xml')
