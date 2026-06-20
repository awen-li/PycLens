# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: HeaderTests_test_parse_ns_headers_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = [[('foo', 'bar'), ('version', '1')]]
    for hdr in ['foo=bar; version="1"', 'foo=bar; Version="1"']:
        self.assertEqual(parse_ns_headers([hdr]), expected)
