# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_redirect_fragment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    redirected_url = 'http://www.example.com/index.html#OK\r\n\r\n'
    hh = MockHTTPHandler(302, 'Location: ' + redirected_url)
    hdeh = urllib.request.HTTPDefaultErrorHandler()
    hrh = urllib.request.HTTPRedirectHandler()
    o = build_test_opener(hh, hdeh, hrh)
    fp = o.open('http://www.example.com')
    self.assertEqual(fp.geturl(), redirected_url.strip())
