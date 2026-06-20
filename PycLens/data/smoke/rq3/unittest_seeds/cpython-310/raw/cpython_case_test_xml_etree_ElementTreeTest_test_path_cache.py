# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_path_cache

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from xml.etree import ElementPath
    elem = ET.XML(SAMPLE_XML)
    for i in range(10):
        ET.ElementTree(elem).find('./' + str(i))
    cache_len_10 = len(ElementPath._cache)
    for i in range(10):
        ET.ElementTree(elem).find('./' + str(i))
    self.assertEqual(len(ElementPath._cache), cache_len_10)
    for i in range(20):
        ET.ElementTree(elem).find('./' + str(i))
    self.assertGreater(len(ElementPath._cache), cache_len_10)
    for i in range(600):
        ET.ElementTree(elem).find('./' + str(i))
    self.assertLess(len(ElementPath._cache), 500)
