# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: OtherNetworkTests_test_custom_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    url = support.TEST_HTTP_URL
    with socket_helper.transient_internet(url):
        opener = urllib.request.build_opener()
        request = urllib.request.Request(url)
        self.assertFalse(request.header_items())
        opener.open(request)
        self.assertTrue(request.header_items())
        self.assertTrue(request.has_header('User-agent'))
        request.add_header('User-Agent', 'Test-Agent')
        opener.open(request)
        self.assertEqual(request.get_header('User-agent'), 'Test-Agent')
