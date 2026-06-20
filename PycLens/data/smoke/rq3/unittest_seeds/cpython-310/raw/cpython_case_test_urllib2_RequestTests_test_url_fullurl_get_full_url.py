# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestTests_test_url_fullurl_get_full_url

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    urls = ['http://docs.python.org', 'http://docs.python.org/library/urllib2.html#OK', 'http://www.python.org/?qs=query#fragment=true']
    for url in urls:
        req = Request(url)
        self.assertEqual(req.get_full_url(), req.full_url)
