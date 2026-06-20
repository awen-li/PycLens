# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_RFC2732

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    str_cases = [('http://Test.python.org:5432/foo/', 'test.python.org', 5432), ('http://12.34.56.78:5432/foo/', '12.34.56.78', 5432), ('http://[::1]:5432/foo/', '::1', 5432), ('http://[dead:beef::1]:5432/foo/', 'dead:beef::1', 5432), ('http://[dead:beef::]:5432/foo/', 'dead:beef::', 5432), ('http://[dead:beef:cafe:5417:affe:8FA3:deaf:feed]:5432/foo/', 'dead:beef:cafe:5417:affe:8fa3:deaf:feed', 5432), ('http://[::12.34.56.78]:5432/foo/', '::12.34.56.78', 5432), ('http://[::ffff:12.34.56.78]:5432/foo/', '::ffff:12.34.56.78', 5432), ('http://Test.python.org/foo/', 'test.python.org', None), ('http://12.34.56.78/foo/', '12.34.56.78', None), ('http://[::1]/foo/', '::1', None), ('http://[dead:beef::1]/foo/', 'dead:beef::1', None), ('http://[dead:beef::]/foo/', 'dead:beef::', None), ('http://[dead:beef:cafe:5417:affe:8FA3:deaf:feed]/foo/', 'dead:beef:cafe:5417:affe:8fa3:deaf:feed', None), ('http://[::12.34.56.78]/foo/', '::12.34.56.78', None), ('http://[::ffff:12.34.56.78]/foo/', '::ffff:12.34.56.78', None), ('http://Test.python.org:/foo/', 'test.python.org', None), ('http://12.34.56.78:/foo/', '12.34.56.78', None), ('http://[::1]:/foo/', '::1', None), ('http://[dead:beef::1]:/foo/', 'dead:beef::1', None), ('http://[dead:beef::]:/foo/', 'dead:beef::', None), ('http://[dead:beef:cafe:5417:affe:8FA3:deaf:feed]:/foo/', 'dead:beef:cafe:5417:affe:8fa3:deaf:feed', None), ('http://[::12.34.56.78]:/foo/', '::12.34.56.78', None), ('http://[::ffff:12.34.56.78]:/foo/', '::ffff:12.34.56.78', None)]

    def _encode(t):
        return (t[0].encode('ascii'), t[1].encode('ascii'), t[2])
    bytes_cases = [_encode(x) for x in str_cases]
    for (url, hostname, port) in str_cases + bytes_cases:
        urlparsed = urllib.parse.urlparse(url)
        self.assertEqual((urlparsed.hostname, urlparsed.port), (hostname, port))
    str_cases = ['http://::12.34.56.78]/', 'http://[::1/foo/', 'ftp://[::1/foo/bad]/bad', 'http://[::1/foo/bad]/bad', 'http://[::ffff:12.34.56.78']
    bytes_cases = [x.encode('ascii') for x in str_cases]
    for invalid_url in str_cases + bytes_cases:
        self.assertRaises(ValueError, urllib.parse.urlparse, invalid_url)
