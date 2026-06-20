# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestTests_test_url_fragment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    req = Request('http://www.python.org/?qs=query#fragment=true')
    self.assertEqual('/?qs=query', req.selector)
    req = Request('http://www.python.org/#fun=true')
    self.assertEqual('/', req.selector)
    url = 'http://docs.python.org/library/urllib2.html#OK'
    req = Request(url)
    self.assertEqual(req.get_full_url(), url)
