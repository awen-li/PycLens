# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementFindTest_test_find_through_ElementTree

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.XML(SAMPLE_XML)
    self.assertEqual(ET.ElementTree(e).find('tag').tag, 'tag')
    self.assertEqual(ET.ElementTree(e).findtext('tag'), 'text')
    self.assertEqual(summarize_list(ET.ElementTree(e).findall('tag')), ['tag'] * 2)
    msg = "This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to '.+'"
    with self.assertWarnsRegex(FutureWarning, msg):
        it = ET.ElementTree(e).findall('//tag')
    self.assertEqual(summarize_list(it), ['tag'] * 3)
