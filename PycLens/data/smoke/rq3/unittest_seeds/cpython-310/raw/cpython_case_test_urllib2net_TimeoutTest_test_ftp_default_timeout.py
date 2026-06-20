# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: TimeoutTest_test_ftp_default_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsNone(socket.getdefaulttimeout())
    with socket_helper.transient_internet(self.FTP_HOST):
        socket.setdefaulttimeout(60)
        try:
            u = _urlopen_with_retry(self.FTP_HOST)
            self.addCleanup(u.close)
        finally:
            socket.setdefaulttimeout(None)
        self.assertEqual(u.fp.fp.raw._sock.gettimeout(), 60)
