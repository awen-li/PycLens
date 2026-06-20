# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XIncludeTest_test_xinclude

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from xml.etree import ElementInclude
    document = self.xinclude_loader('C1.xml')
    ElementInclude.include(document, self.xinclude_loader)
    self.assertEqual(serialize(document), '<document>\n  <p>120 Mz is adequate for an average home user.</p>\n  <disclaimer>\n  <p>The opinions represented herein represent those of the individual\n  and should not be interpreted as official policy endorsed by this\n  organization.</p>\n</disclaimer>\n</document>')
    document = self.xinclude_loader('C2.xml')
    ElementInclude.include(document, self.xinclude_loader)
    self.assertEqual(serialize(document), '<document>\n  <p>This document has been accessed\n  324387 times.</p>\n</document>')
    document = self.xinclude_loader('C2b.xml')
    ElementInclude.include(document, self.xinclude_loader)
    self.assertEqual(serialize(document), '<document>\n  <p>This document has been <em>accessed</em>\n  324387 times.</p>\n</document>')
    document = self.xinclude_loader('C3.xml')
    ElementInclude.include(document, self.xinclude_loader)
    self.assertEqual(serialize(document), '<document>\n  <p>The following is the source of the "data.xml" resource:</p>\n  <example>&lt;?xml version=\'1.0\'?&gt;\n&lt;data&gt;\n  &lt;item&gt;&lt;![CDATA[Brooks &amp; Shields]]&gt;&lt;/item&gt;\n&lt;/data&gt;\n</example>\n</document>')
    document = self.xinclude_loader('C5.xml')
    with self.assertRaises(OSError) as cm:
        ElementInclude.include(document, self.xinclude_loader)
    self.assertEqual(str(cm.exception), 'resource not found')
    self.assertEqual(serialize(document), '<div xmlns:ns0="http://www.w3.org/2001/XInclude">\n  <ns0:include href="example.txt" parse="text">\n    <ns0:fallback>\n      <ns0:include href="fallback-example.txt" parse="text">\n        <ns0:fallback><a href="mailto:bob@example.org">Report error</a></ns0:fallback>\n      </ns0:include>\n    </ns0:fallback>\n  </ns0:include>\n</div>')
