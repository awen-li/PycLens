# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: TimeoutTest_test_ftp_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsNone(socket.getdefaulttimeout())
    with socket_helper.transient_internet(self.FTP_HOST, timeout=None):
        u = _urlopen_with_retry(self.FTP_HOST)
        self.addCleanup(u.close)
        self.assertIsNone(u.fp.fp.raw._sock.gettimeout())
