# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: TimeoutTest_test_http_no_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsNone(socket.getdefaulttimeout())
    url = support.TEST_HTTP_URL
    with socket_helper.transient_internet(url):
        socket.setdefaulttimeout(60)
        try:
            u = _urlopen_with_retry(url, timeout=None)
            self.addCleanup(u.close)
        finally:
            socket.setdefaulttimeout(None)
        self.assertIsNone(u.fp.raw._sock.gettimeout())
