# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementFindTest_test_bad_find

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.XML(SAMPLE_XML)
    with self.assertRaisesRegex(SyntaxError, 'cannot use absolute path'):
        e.findall('/tag')
