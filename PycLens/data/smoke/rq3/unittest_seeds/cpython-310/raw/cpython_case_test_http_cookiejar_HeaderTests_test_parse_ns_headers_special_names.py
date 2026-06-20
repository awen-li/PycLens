# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: HeaderTests_test_parse_ns_headers_special_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hdr = 'expires=01 Jan 2040 22:23:32 GMT'
    expected = [[('expires', '01 Jan 2040 22:23:32 GMT'), ('version', '0')]]
    self.assertEqual(parse_ns_headers([hdr]), expected)
