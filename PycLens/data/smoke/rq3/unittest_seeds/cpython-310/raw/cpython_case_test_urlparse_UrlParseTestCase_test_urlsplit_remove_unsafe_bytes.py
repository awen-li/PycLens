# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_urlsplit_remove_unsafe_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    url = "http\t://www.python\n.org\t/java\nscript:\talert('msg\r\n')/?query\n=\tsomething#frag\nment"
    p = urllib.parse.urlsplit(url)
    self.assertEqual(p.scheme, 'http')
    self.assertEqual(p.netloc, 'www.python.org')
    self.assertEqual(p.path, "/javascript:alert('msg')/")
    self.assertEqual(p.query, 'query=something')
    self.assertEqual(p.fragment, 'fragment')
    self.assertEqual(p.username, None)
    self.assertEqual(p.password, None)
    self.assertEqual(p.hostname, 'www.python.org')
    self.assertEqual(p.port, None)
    self.assertEqual(p.geturl(), "http://www.python.org/javascript:alert('msg')/?query=something#fragment")
    url = b"http\t://www.python\n.org\t/java\nscript:\talert('msg\r\n')/?query\n=\tsomething#frag\nment"
    p = urllib.parse.urlsplit(url)
    self.assertEqual(p.scheme, b'http')
    self.assertEqual(p.netloc, b'www.python.org')
    self.assertEqual(p.path, b"/javascript:alert('msg')/")
    self.assertEqual(p.query, b'query=something')
    self.assertEqual(p.fragment, b'fragment')
    self.assertEqual(p.username, None)
    self.assertEqual(p.password, None)
    self.assertEqual(p.hostname, b'www.python.org')
    self.assertEqual(p.port, None)
    self.assertEqual(p.geturl(), b"http://www.python.org/javascript:alert('msg')/?query=something#fragment")
    url = "http://www.python.org/java\nscript:\talert('msg\r\n')/?query\n=\tsomething#frag\nment"
    scheme = 'ht\ntp'
    for _ in range(2):
        p = urllib.parse.urlsplit(url, scheme=scheme)
        self.assertEqual(p.scheme, 'http')
        self.assertEqual(p.geturl(), "http://www.python.org/javascript:alert('msg')/?query=something#fragment")
