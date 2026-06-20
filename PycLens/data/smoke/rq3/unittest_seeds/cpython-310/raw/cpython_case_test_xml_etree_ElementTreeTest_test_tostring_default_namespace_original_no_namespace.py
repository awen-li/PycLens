# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_tostring_default_namespace_original_no_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<body><tag/></body>')
    EXPECTED_MSG = '^cannot use non-qualified names with default_namespace option$'
    with self.assertRaisesRegex(ValueError, EXPECTED_MSG):
        ET.tostring(elem, encoding='unicode', default_namespace='foobar')
