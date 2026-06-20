# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: HeaderTests_test_parse_ns_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = [[('foo', 'bar'), ('expires', 2209069412), ('version', '0')]]
    for hdr in ['foo=bar; expires=01 Jan 2040 22:23:32 GMT', 'foo=bar; expires="01 Jan 2040 22:23:32 GMT"']:
        self.assertEqual(parse_ns_headers([hdr]), expected)
