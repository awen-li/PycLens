# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: TimeoutTest_test_http_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    url = support.TEST_HTTP_URL
    with socket_helper.transient_internet(url):
        u = _urlopen_with_retry(url, timeout=120)
        self.addCleanup(u.close)
        self.assertEqual(u.fp.raw._sock.gettimeout(), 120)
