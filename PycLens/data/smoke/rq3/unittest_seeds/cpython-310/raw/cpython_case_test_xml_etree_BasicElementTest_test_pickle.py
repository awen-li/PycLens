# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BasicElementTest_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(2, pickle.HIGHEST_PROTOCOL + 1):
        for (dumper, loader) in product(self.modules, repeat=2):
            e = dumper.Element('foo', bar=42)
            e.text = 'text goes here'
            e.tail = 'opposite of head'
            dumper.SubElement(e, 'child').append(dumper.Element('grandchild'))
            e.append(dumper.Element('child'))
            e.findall('.//grandchild')[0].set('attr', 'other value')
            e2 = self.pickleRoundTrip(e, 'xml.etree.ElementTree', dumper, loader, proto)
            self.assertEqual(e2.tag, 'foo')
            self.assertEqual(e2.attrib['bar'], 42)
            self.assertEqual(len(e2), 2)
            self.assertEqualElements(e, e2)
