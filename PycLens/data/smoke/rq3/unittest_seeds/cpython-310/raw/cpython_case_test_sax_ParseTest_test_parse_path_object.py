# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ParseTest_test_parse_path_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    make_xml_file(self.data, 'utf-8', None)
    self.check_parse(FakePath(TESTFN))
