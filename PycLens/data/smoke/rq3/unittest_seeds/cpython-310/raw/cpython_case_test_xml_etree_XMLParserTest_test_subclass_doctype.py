# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLParserTest_test_subclass_doctype

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _doctype = None

    class MyParserWithDoctype(ET.XMLParser):

        def doctype(self, *args, **kwargs):
            nonlocal _doctype
            _doctype = (args, kwargs)
    parser = MyParserWithDoctype()
    with self.assertWarnsRegex(RuntimeWarning, 'doctype'):
        parser.feed(self.sample2)
    parser.close()
    self.assertIsNone(_doctype)
    _doctype = _doctype2 = None
    with warnings.catch_warnings():
        warnings.simplefilter('error', DeprecationWarning)
        warnings.simplefilter('error', RuntimeWarning)

        class DoctypeParser:

            def doctype(self, name, pubid, system):
                nonlocal _doctype2
                _doctype2 = (name, pubid, system)
        parser = MyParserWithDoctype(target=DoctypeParser())
        parser.feed(self.sample2)
        parser.close()
        self.assertIsNone(_doctype)
        self.assertEqual(_doctype2, ('html', '-//W3C//DTD XHTML 1.0 Transitional//EN', 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'))
