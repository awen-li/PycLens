# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_xmltoolkit62

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ENTITIES = {'rsquo': '’', 'lsquo': '‘'}
    parser = ET.XMLParser()
    parser.entity.update(ENTITIES)
    parser.feed('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE patent-application-publication SYSTEM "pap-v15-2001-01-31.dtd" []>\n<patent-application-publication>\n<subdoc-abstract>\n<paragraph id="A-0001" lvl="0">A new cultivar of Begonia plant named &lsquo;BCT9801BEG&rsquo;.</paragraph>\n</subdoc-abstract>\n</patent-application-publication>')
    t = parser.close()
    self.assertEqual(t.find('.//paragraph').text, 'A new cultivar of Begonia plant named ‘BCT9801BEG’.')
