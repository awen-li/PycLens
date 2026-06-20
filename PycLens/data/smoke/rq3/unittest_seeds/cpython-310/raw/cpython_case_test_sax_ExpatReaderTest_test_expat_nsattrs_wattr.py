# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_nsattrs_wattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = create_parser(1)
    gather = self.AttrGatherer()
    parser.setContentHandler(gather)
    parser.feed("<doc xmlns:ns='%s' ns:attr='val'/>" % ns_uri)
    parser.close()
    attrs = gather._attrs
    self.assertEqual(attrs.getLength(), 1)
    self.assertEqual(attrs.getNames(), [(ns_uri, 'attr')])
    self.assertTrue(attrs.getQNames() == [] or attrs.getQNames() == ['ns:attr'])
    self.assertEqual(len(attrs), 1)
    self.assertIn((ns_uri, 'attr'), attrs)
    self.assertEqual(attrs.get((ns_uri, 'attr')), 'val')
    self.assertEqual(attrs.get((ns_uri, 'attr'), 25), 'val')
    self.assertEqual(list(attrs.items()), [((ns_uri, 'attr'), 'val')])
    self.assertEqual(list(attrs.values()), ['val'])
    self.assertEqual(attrs.getValue((ns_uri, 'attr')), 'val')
    self.assertEqual(attrs[ns_uri, 'attr'], 'val')
