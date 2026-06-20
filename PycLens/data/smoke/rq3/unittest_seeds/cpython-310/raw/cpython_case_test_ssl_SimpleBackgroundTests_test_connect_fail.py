# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_connect_fail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = test_wrap_socket(socket.socket(socket.AF_INET), cert_reqs=ssl.CERT_REQUIRED)
    self.addCleanup(s.close)
    self.assertRaisesRegex(ssl.SSLError, 'certificate verify failed', s.connect, self.server_addr)
