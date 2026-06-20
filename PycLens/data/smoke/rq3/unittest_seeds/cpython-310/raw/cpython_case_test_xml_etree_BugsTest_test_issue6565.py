# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_issue6565

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<body><tag/></body>')
    self.assertEqual(summarize_list(elem), ['tag'])
    newelem = ET.XML(SAMPLE_XML)
    elem[:] = newelem[:]
    self.assertEqual(summarize_list(elem), ['tag', 'tag', 'section'])
