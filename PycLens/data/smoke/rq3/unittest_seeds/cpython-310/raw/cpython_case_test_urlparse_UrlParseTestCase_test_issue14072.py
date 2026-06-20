# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_issue14072

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p1 = urllib.parse.urlsplit('tel:+31-641044153')
    self.assertEqual(p1.scheme, 'tel')
    self.assertEqual(p1.path, '+31-641044153')
    p2 = urllib.parse.urlsplit('tel:+31641044153')
    self.assertEqual(p2.scheme, 'tel')
    self.assertEqual(p2.path, '+31641044153')
    p1 = urllib.parse.urlparse('tel:+31-641044153')
    self.assertEqual(p1.scheme, 'tel')
    self.assertEqual(p1.path, '+31-641044153')
    p2 = urllib.parse.urlparse('tel:+31641044153')
    self.assertEqual(p2.scheme, 'tel')
    self.assertEqual(p2.path, '+31641044153')
