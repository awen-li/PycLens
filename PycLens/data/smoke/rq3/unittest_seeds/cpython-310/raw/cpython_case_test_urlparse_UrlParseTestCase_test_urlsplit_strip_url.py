# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_urlsplit_strip_url

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    noise = bytes(range(0, 32 + 1))
    base_url = 'http://User:Pass@www.python.org:080/doc/?query=yes#frag'
    url = noise.decode('utf-8') + base_url
    p = urllib.parse.urlsplit(url)
    self.assertEqual(p.scheme, 'http')
    self.assertEqual(p.netloc, 'User:Pass@www.python.org:080')
    self.assertEqual(p.path, '/doc/')
    self.assertEqual(p.query, 'query=yes')
    self.assertEqual(p.fragment, 'frag')
    self.assertEqual(p.username, 'User')
    self.assertEqual(p.password, 'Pass')
    self.assertEqual(p.hostname, 'www.python.org')
    self.assertEqual(p.port, 80)
    self.assertEqual(p.geturl(), base_url)
    url = noise + base_url.encode('utf-8')
    p = urllib.parse.urlsplit(url)
    self.assertEqual(p.scheme, b'http')
    self.assertEqual(p.netloc, b'User:Pass@www.python.org:080')
    self.assertEqual(p.path, b'/doc/')
    self.assertEqual(p.query, b'query=yes')
    self.assertEqual(p.fragment, b'frag')
    self.assertEqual(p.username, b'User')
    self.assertEqual(p.password, b'Pass')
    self.assertEqual(p.hostname, b'www.python.org')
    self.assertEqual(p.port, 80)
    self.assertEqual(p.geturl(), base_url.encode('utf-8'))
    query_spaces_url = 'https://www.python.org:88/doc/?query=    '
    p = urllib.parse.urlsplit(noise.decode('utf-8') + query_spaces_url)
    self.assertEqual(p.scheme, 'https')
    self.assertEqual(p.netloc, 'www.python.org:88')
    self.assertEqual(p.path, '/doc/')
    self.assertEqual(p.query, 'query=    ')
    self.assertEqual(p.port, 88)
    self.assertEqual(p.geturl(), query_spaces_url)
    p = urllib.parse.urlsplit('www.pypi.org ')
    self.assertEqual(urllib.parse.urlunsplit(p), 'www.pypi.org ')
    url = '//www.python.org/'
    scheme = noise.decode('utf-8') + 'https' + noise.decode('utf-8')
    for _ in range(2):
        p = urllib.parse.urlsplit(url, scheme=scheme)
        self.assertEqual(p.scheme, 'https')
        self.assertEqual(p.geturl(), 'https://www.python.org/')
