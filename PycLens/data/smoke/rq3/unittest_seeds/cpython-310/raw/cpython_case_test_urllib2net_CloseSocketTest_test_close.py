# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: CloseSocketTest_test_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(urllib.request.urlcleanup)
    url = support.TEST_HTTP_URL
    with socket_helper.transient_internet(url):
        response = _urlopen_with_retry(url)
        sock = response.fp
        self.assertFalse(sock.closed)
        response.close()
        self.assertTrue(sock.closed)
