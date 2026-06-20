# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlReaderTest_test_nsattrs_wattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    attrs = AttributesNSImpl({(ns_uri, 'attr'): 'val'}, {(ns_uri, 'attr'): 'ns:attr'})
    self.assertEqual(attrs.getLength(), 1)
    self.assertEqual(attrs.getNames(), [(ns_uri, 'attr')])
    self.assertEqual(attrs.getQNames(), ['ns:attr'])
    self.assertEqual(len(attrs), 1)
    self.assertIn((ns_uri, 'attr'), attrs)
    self.assertEqual(list(attrs.keys()), [(ns_uri, 'attr')])
    self.assertEqual(attrs.get((ns_uri, 'attr')), 'val')
    self.assertEqual(attrs.get((ns_uri, 'attr'), 25), 'val')
    self.assertEqual(list(attrs.items()), [((ns_uri, 'attr'), 'val')])
    self.assertEqual(list(attrs.values()), ['val'])
    self.assertEqual(attrs.getValue((ns_uri, 'attr')), 'val')
    self.assertEqual(attrs.getValueByQName('ns:attr'), 'val')
    self.assertEqual(attrs.getNameByQName('ns:attr'), (ns_uri, 'attr'))
    self.assertEqual(attrs[ns_uri, 'attr'], 'val')
    self.assertEqual(attrs.getQNameByName((ns_uri, 'attr')), 'ns:attr')
