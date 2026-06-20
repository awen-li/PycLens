# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_strict_domain

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cp = DefaultCookiePolicy(strict_domain=True)
    cj = CookieJar(policy=cp)
    interact_netscape(cj, 'http://example.co.uk/', 'no=problemo')
    interact_netscape(cj, 'http://example.co.uk/', 'okey=dokey; Domain=.example.co.uk')
    self.assertEqual(len(cj), 2)
    for pseudo_tld in ['.co.uk', '.org.za', '.tx.us', '.name.us']:
        interact_netscape(cj, 'http://example.%s/' % pseudo_tld, 'spam=eggs; Domain=.co.uk')
        self.assertEqual(len(cj), 2)
