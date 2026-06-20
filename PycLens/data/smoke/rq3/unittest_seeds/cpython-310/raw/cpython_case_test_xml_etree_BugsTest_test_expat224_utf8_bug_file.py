# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_expat224_utf8_bug_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(UTF8_BUG_XMLFILE, 'rb') as fp:
        raw = fp.read()
    root = ET.fromstring(raw)
    xmlattr = root.get('b')
    text = raw.decode('utf-8').strip()
    text = text.replace('\r\n', ' ')
    text = text[6:-4]
    self.assertEqual(root.get('b'), text)
