# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_parse_ns_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(parse_ns_headers(['foo=bar; path=/; domain']), [[('foo', 'bar'), ('path', '/'), ('domain', None), ('version', '0')]])
    self.assertEqual(parse_ns_headers(['foo=bar; expires=Foo Bar 12 33:22:11 2000']), [[('foo', 'bar'), ('expires', None), ('version', '0')]])
    self.assertEqual(parse_ns_headers(['foo']), [[('foo', None), ('version', '0')]])
    self.assertEqual(parse_ns_headers(['foo=bar; expires']), [[('foo', 'bar'), ('expires', None), ('version', '0')]])
    self.assertEqual(parse_ns_headers(['foo=bar; version']), [[('foo', 'bar'), ('version', None)]])
    self.assertEqual(parse_ns_headers(['']), [])
