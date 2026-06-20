# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_connect_ex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = test_wrap_socket(socket.socket(socket.AF_INET), cert_reqs=ssl.CERT_REQUIRED, ca_certs=SIGNING_CA)
    self.addCleanup(s.close)
    self.assertEqual(0, s.connect_ex(self.server_addr))
    self.assertTrue(s.getpeercert())
