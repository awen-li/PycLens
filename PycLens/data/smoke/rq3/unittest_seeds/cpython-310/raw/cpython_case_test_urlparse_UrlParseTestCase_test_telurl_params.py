# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_telurl_params

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p1 = urllib.parse.urlparse('tel:123-4;phone-context=+1-650-516')
    self.assertEqual(p1.scheme, 'tel')
    self.assertEqual(p1.path, '123-4')
    self.assertEqual(p1.params, 'phone-context=+1-650-516')
    p1 = urllib.parse.urlparse('tel:+1-201-555-0123')
    self.assertEqual(p1.scheme, 'tel')
    self.assertEqual(p1.path, '+1-201-555-0123')
    self.assertEqual(p1.params, '')
    p1 = urllib.parse.urlparse('tel:7042;phone-context=example.com')
    self.assertEqual(p1.scheme, 'tel')
    self.assertEqual(p1.path, '7042')
    self.assertEqual(p1.params, 'phone-context=example.com')
    p1 = urllib.parse.urlparse('tel:863-1234;phone-context=+1-914-555')
    self.assertEqual(p1.scheme, 'tel')
    self.assertEqual(p1.path, '863-1234')
    self.assertEqual(p1.params, 'phone-context=+1-914-555')
