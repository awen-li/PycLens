# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BasicElementTest_test_pickle_issue18997

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(2, pickle.HIGHEST_PROTOCOL + 1):
        for (dumper, loader) in product(self.modules, repeat=2):
            XMLTEXT = '<?xml version="1.0"?>\n                    <group><dogs>4</dogs>\n                    </group>'
            e1 = dumper.fromstring(XMLTEXT)
            if hasattr(e1, '__getstate__'):
                self.assertEqual(e1.__getstate__()['tag'], 'group')
            e2 = self.pickleRoundTrip(e1, 'xml.etree.ElementTree', dumper, loader, proto)
            self.assertEqual(e2.tag, 'group')
            self.assertEqual(e2[0].tag, 'dogs')
