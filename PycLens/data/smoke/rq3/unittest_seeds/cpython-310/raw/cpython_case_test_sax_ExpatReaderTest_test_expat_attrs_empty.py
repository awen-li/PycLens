# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_attrs_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = create_parser()
    gather = self.AttrGatherer()
    parser.setContentHandler(gather)
    parser.feed('<doc/>')
    parser.close()
    self.verify_empty_attrs(gather._attrs)
