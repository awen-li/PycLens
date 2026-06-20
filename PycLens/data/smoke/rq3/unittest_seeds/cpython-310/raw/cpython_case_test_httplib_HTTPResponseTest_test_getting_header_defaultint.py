# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPResponseTest_test_getting_header_defaultint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    header = self.resp.getheader('No-Such-Header', default=42)
    self.assertEqual(header, 42)
