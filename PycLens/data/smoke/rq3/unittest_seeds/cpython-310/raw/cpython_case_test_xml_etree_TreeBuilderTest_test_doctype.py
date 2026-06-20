# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_doctype

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class DoctypeParser:
        _doctype = None

        def doctype(self, name, pubid, system):
            self._doctype = (name, pubid, system)

        def close(self):
            return self._doctype
    parser = ET.XMLParser(target=DoctypeParser())
    parser.feed(self.sample1)
    self.assertEqual(parser.close(), ('html', '-//W3C//DTD XHTML 1.0 Transitional//EN', 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'))
