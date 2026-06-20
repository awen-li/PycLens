# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: MiscTests_test_uninitialized_parser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = cET.XMLParser.__new__(cET.XMLParser)
    self.assertRaises(ValueError, parser.close)
    self.assertRaises(ValueError, parser.feed, 'foo')

    class MockFile:

        def read(*args):
            return ''
    self.assertRaises(ValueError, parser._parse_whole, MockFile())
    self.assertRaises(ValueError, parser._setevents, None)
    self.assertIsNone(parser.entity)
    self.assertIsNone(parser.target)
