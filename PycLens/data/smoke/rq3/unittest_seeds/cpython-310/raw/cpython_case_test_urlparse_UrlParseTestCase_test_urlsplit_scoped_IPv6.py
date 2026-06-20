# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_urlsplit_scoped_IPv6

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = urllib.parse.urlsplit('http://[FE80::822a:a8ff:fe49:470c%tESt]:1234')
    self.assertEqual(p.hostname, 'fe80::822a:a8ff:fe49:470c%tESt')
    self.assertEqual(p.netloc, '[FE80::822a:a8ff:fe49:470c%tESt]:1234')
    p = urllib.parse.urlsplit(b'http://[FE80::822a:a8ff:fe49:470c%tESt]:1234')
    self.assertEqual(p.hostname, b'fe80::822a:a8ff:fe49:470c%tESt')
    self.assertEqual(p.netloc, b'[FE80::822a:a8ff:fe49:470c%tESt]:1234')
