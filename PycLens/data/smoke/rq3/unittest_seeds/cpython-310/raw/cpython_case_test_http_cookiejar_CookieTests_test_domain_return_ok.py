# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_domain_return_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pol = DefaultCookiePolicy()
    for (url, domain, ok) in [('http://foo.bar.com/', 'blah.com', False), ('http://foo.bar.com/', 'rhubarb.blah.com', False), ('http://foo.bar.com/', 'rhubarb.foo.bar.com', False), ('http://foo.bar.com/', '.foo.bar.com', True), ('http://foo.bar.com/', 'foo.bar.com', True), ('http://foo.bar.com/', '.bar.com', True), ('http://foo.bar.com/', 'bar.com', True), ('http://foo.bar.com/', 'com', True), ('http://foo.com/', 'rhubarb.foo.com', False), ('http://foo.com/', '.foo.com', True), ('http://foo.com/', 'foo.com', True), ('http://foo.com/', 'com', True), ('http://foo/', 'rhubarb.foo', False), ('http://foo/', '.foo', True), ('http://foo/', 'foo', True), ('http://foo/', 'foo.local', True), ('http://foo/', '.local', True), ('http://barfoo.com', '.foo.com', False), ('http://barfoo.com', 'foo.com', False)]:
        request = urllib.request.Request(url)
        r = pol.domain_return_ok(domain, request)
        if ok:
            self.assertTrue(r)
        else:
            self.assertFalse(r)
