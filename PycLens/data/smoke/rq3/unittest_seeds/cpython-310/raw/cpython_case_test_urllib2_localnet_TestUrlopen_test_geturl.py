# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_geturl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = self.start_server()
    open_url = urllib.request.urlopen('http://localhost:%s' % handler.port)
    with open_url:
        url = open_url.geturl()
    self.assertEqual(url, 'http://localhost:%s' % handler.port)
