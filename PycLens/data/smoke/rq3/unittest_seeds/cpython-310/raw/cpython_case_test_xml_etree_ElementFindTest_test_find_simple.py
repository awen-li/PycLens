# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementFindTest_test_find_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.XML(SAMPLE_XML)
    self.assertEqual(e.find('tag').tag, 'tag')
    self.assertEqual(e.find('section/tag').tag, 'tag')
    self.assertEqual(e.find('./tag').tag, 'tag')
    e[2] = ET.XML(SAMPLE_SECTION)
    self.assertEqual(e.find('section/nexttag').tag, 'nexttag')
    self.assertEqual(e.findtext('./tag'), 'text')
    self.assertEqual(e.findtext('section/tag'), 'subtext')
    self.assertEqual(e.findtext('section/nexttag'), '')
    self.assertEqual(e.findtext('section/nexttag', 'default'), '')
    self.assertIsNone(e.findtext('tog'))
    self.assertEqual(e.findtext('tog', 'default'), 'default')
    self.assertEqual(ET.XML('<tag><empty /></tag>').findtext('empty'), '')
