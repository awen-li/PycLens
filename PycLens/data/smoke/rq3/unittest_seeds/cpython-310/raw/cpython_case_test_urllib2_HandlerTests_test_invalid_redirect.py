# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_invalid_redirect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from_url = 'http://example.com/a.html'
    valid_schemes = ['http', 'https', 'ftp']
    invalid_schemes = ['file', 'imap', 'ldap']
    schemeless_url = 'example.com/b.html'
    h = urllib.request.HTTPRedirectHandler()
    o = h.parent = MockOpener()
    req = Request(from_url)
    req.timeout = socket._GLOBAL_DEFAULT_TIMEOUT
    for scheme in invalid_schemes:
        invalid_url = scheme + '://' + schemeless_url
        self.assertRaises(urllib.error.HTTPError, h.http_error_302, req, MockFile(), 302, 'Security Loophole', MockHeaders({'location': invalid_url}))
    for scheme in valid_schemes:
        valid_url = scheme + '://' + schemeless_url
        h.http_error_302(req, MockFile(), 302, "That's fine", MockHeaders({'location': valid_url}))
        self.assertEqual(o.req.get_full_url(), valid_url)
