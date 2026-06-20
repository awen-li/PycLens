# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_tostringlist_default_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<body xmlns="http://effbot.org/ns"><tag/></body>')
    self.assertEqual(''.join(ET.tostringlist(elem, encoding='unicode')), '<ns0:body xmlns:ns0="http://effbot.org/ns"><ns0:tag /></ns0:body>')
    self.assertEqual(''.join(ET.tostringlist(elem, encoding='unicode', default_namespace='http://effbot.org/ns')), '<body xmlns="http://effbot.org/ns"><tag /></body>')
