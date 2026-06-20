# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_attributes_without_netloc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    uri = 'sip:alice@atlanta.com;maddr=239.255.255.1;ttl=15'
    p = urllib.parse.urlsplit(uri)
    self.assertEqual(p.netloc, '')
    self.assertEqual(p.username, None)
    self.assertEqual(p.password, None)
    self.assertEqual(p.hostname, None)
    self.assertEqual(p.port, None)
    self.assertEqual(p.geturl(), uri)
    p = urllib.parse.urlparse(uri)
    self.assertEqual(p.netloc, '')
    self.assertEqual(p.username, None)
    self.assertEqual(p.password, None)
    self.assertEqual(p.hostname, None)
    self.assertEqual(p.port, None)
    self.assertEqual(p.geturl(), uri)
    uri = b'sip:alice@atlanta.com;maddr=239.255.255.1;ttl=15'
    p = urllib.parse.urlsplit(uri)
    self.assertEqual(p.netloc, b'')
    self.assertEqual(p.username, None)
    self.assertEqual(p.password, None)
    self.assertEqual(p.hostname, None)
    self.assertEqual(p.port, None)
    self.assertEqual(p.geturl(), uri)
    p = urllib.parse.urlparse(uri)
    self.assertEqual(p.netloc, b'')
    self.assertEqual(p.username, None)
    self.assertEqual(p.password, None)
    self.assertEqual(p.hostname, None)
    self.assertEqual(p.port, None)
    self.assertEqual(p.geturl(), uri)
