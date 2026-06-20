# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    global pyET
    pyET = import_fresh_module('xml.etree.ElementTree', blocked=['_elementtree'])
    if module is None:
        module = pyET
    global ET
    ET = module
    test_classes = [ModuleTest, ElementSlicingTest, BasicElementTest, BadElementTest, BadElementPathTest, ElementTreeTest, IOTest, ParseErrorTest, XIncludeTest, ElementTreeTypeTest, ElementFindTest, ElementIterTest, TreeBuilderTest, XMLParserTest, XMLPullParserTest, BugsTest, KeywordArgsTest, C14NTest]
    if pyET is not ET:
        test_classes.extend([NoAcceleratorTest])
    from xml.etree import ElementPath
    nsmap = ET.register_namespace._namespace_map
    nsmap_copy = nsmap.copy()
    path_cache = ElementPath._cache
    ElementPath._cache = path_cache.copy()
    if hasattr(ET, '_set_factories'):
        old_factories = ET._set_factories(ET.Comment, ET.PI)
    else:
        old_factories = None
    try:
        support.run_unittest(*test_classes)
    finally:
        from xml.etree import ElementPath
        nsmap.clear()
        nsmap.update(nsmap_copy)
        ElementPath._cache = path_cache
        if old_factories is not None:
            ET._set_factories(*old_factories)
        ET = pyET = None
