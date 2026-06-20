# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_full_url_setter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    urls = ['http://example.com?foo=bar#baz', 'http://example.com?foo=bar&spam=eggs#bash', 'http://example.com']
    r = Request('http://example.com')
    for url in urls:
        r.full_url = url
        parsed = urlparse(url)
        self.assertEqual(r.get_full_url(), url)
        self.assertEqual(r.fragment or '', parsed.fragment)
        self.assertEqual(urlparse(r.get_full_url()).query, parsed.query)
