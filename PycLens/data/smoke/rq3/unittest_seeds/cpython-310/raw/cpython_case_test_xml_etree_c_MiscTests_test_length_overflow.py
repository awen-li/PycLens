# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: MiscTests_test_length_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'x' * size
    parser = cET.XMLParser()
    try:
        self.assertRaises(OverflowError, parser.feed, data)
    finally:
        data = None
