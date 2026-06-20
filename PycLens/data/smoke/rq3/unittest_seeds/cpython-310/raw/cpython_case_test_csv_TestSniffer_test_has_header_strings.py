# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestSniffer_test_has_header_strings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sniffer = csv.Sniffer()
    self.assertFalse(sniffer.has_header(self.sample10))
    self.assertFalse(sniffer.has_header(self.sample11))
