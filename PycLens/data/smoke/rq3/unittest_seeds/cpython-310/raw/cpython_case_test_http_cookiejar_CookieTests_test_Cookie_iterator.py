# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_Cookie_iterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cs = CookieJar(DefaultCookiePolicy(rfc2965=True))
    interact_2965(cs, 'http://blah.spam.org/', 'foo=eggs; Version=1; Comment="does anybody read these?"; CommentURL="http://foo.bar.net/comment.html"')
    interact_netscape(cs, 'http://www.acme.com/blah/', 'spam=bar; secure')
    interact_2965(cs, 'http://www.acme.com/blah/', 'foo=bar; secure; Version=1')
    interact_2965(cs, 'http://www.acme.com/blah/', 'foo=bar; path=/; Version=1')
    interact_2965(cs, 'http://www.sol.no', 'bang=wallop; version=1; domain=".sol.no"; port="90,100, 80,8080"; max-age=100; Comment = "Just kidding! (\\"|\\\\\\\\) "')
    versions = [1, 1, 1, 0, 1]
    names = ['bang', 'foo', 'foo', 'spam', 'foo']
    domains = ['.sol.no', 'blah.spam.org', 'www.acme.com', 'www.acme.com', 'www.acme.com']
    paths = ['/', '/', '/', '/blah', '/blah/']
    for i in range(4):
        i = 0
        for c in cs:
            self.assertIsInstance(c, Cookie)
            self.assertEqual(c.version, versions[i])
            self.assertEqual(c.name, names[i])
            self.assertEqual(c.domain, domains[i])
            self.assertEqual(c.path, paths[i])
            i = i + 1
