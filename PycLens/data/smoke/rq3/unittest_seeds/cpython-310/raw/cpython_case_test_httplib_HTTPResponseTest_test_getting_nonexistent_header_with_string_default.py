# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPResponseTest_test_getting_nonexistent_header_with_string_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    header = self.resp.getheader('No-Such-Header', 'default-value')
    self.assertEqual(header, 'default-value')
