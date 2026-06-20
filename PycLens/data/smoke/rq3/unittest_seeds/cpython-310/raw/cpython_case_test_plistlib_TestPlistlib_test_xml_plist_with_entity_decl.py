# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_xml_plist_with_entity_decl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(plistlib.InvalidFileException, 'XML entity declarations are not supported'):
        plistlib.loads(XML_PLIST_WITH_ENTITY, fmt=plistlib.FMT_XML)
