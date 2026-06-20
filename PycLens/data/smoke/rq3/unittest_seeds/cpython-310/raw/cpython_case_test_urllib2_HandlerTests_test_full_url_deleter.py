# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_full_url_deleter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = Request('http://www.example.com')
    del r.full_url
    self.assertIsNone(r.full_url)
    self.assertIsNone(r.fragment)
    self.assertEqual(r.selector, '')
