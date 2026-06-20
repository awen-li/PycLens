# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_fixpath_in_weirdurls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = urllib.request.AbstractHTTPHandler()
    h.parent = MockOpener()
    weird_url = 'http://www.python.org?getspam'
    req = Request(weird_url)
    newreq = h.do_request_(req)
    self.assertEqual(newreq.host, 'www.python.org')
    self.assertEqual(newreq.selector, '/?getspam')
    url_without_path = 'http://www.python.org'
    req = Request(url_without_path)
    newreq = h.do_request_(req)
    self.assertEqual(newreq.host, 'www.python.org')
    self.assertEqual(newreq.selector, '')
