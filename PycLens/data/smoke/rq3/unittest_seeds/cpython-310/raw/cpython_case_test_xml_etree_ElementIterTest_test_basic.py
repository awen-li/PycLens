# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementIterTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    doc = ET.XML('<html><body>this is a <i>paragraph</i>.</body>..</html>')
    self.assertEqual(self._ilist(doc), ['html', 'body', 'i'])
    self.assertEqual(self._ilist(doc.find('body')), ['body', 'i'])
    self.assertEqual(next(doc.iter()).tag, 'html')
    self.assertEqual(''.join(doc.itertext()), 'this is a paragraph...')
    self.assertEqual(''.join(doc.find('body').itertext()), 'this is a paragraph.')
    self.assertEqual(next(doc.itertext()), 'this is a ')
    sourcefile = serialize(doc, to_string=False)
    self.assertEqual(next(ET.iterparse(sourcefile))[0], 'end')
    sourcefile = serialize(doc, to_string=False)
    parser = ET.XMLParser(target=ET.TreeBuilder())
    self.assertEqual(next(ET.iterparse(sourcefile, parser=parser))[0], 'end')
    tree = ET.ElementTree(None)
    self.assertRaises(AttributeError, tree.iter)
    doc = ET.XML('<root>a&amp;<sub>b&amp;</sub>c&amp;</root>')
    self.assertEqual(''.join(doc.itertext()), 'a&b&c&')
