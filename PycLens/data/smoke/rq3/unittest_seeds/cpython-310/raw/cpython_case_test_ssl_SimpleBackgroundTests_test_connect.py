# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_connect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with test_wrap_socket(socket.socket(socket.AF_INET), cert_reqs=ssl.CERT_NONE) as s:
        s.connect(self.server_addr)
        self.assertEqual({}, s.getpeercert())
        self.assertFalse(s.server_side)
    with test_wrap_socket(socket.socket(socket.AF_INET), cert_reqs=ssl.CERT_REQUIRED, ca_certs=SIGNING_CA) as s:
        s.connect(self.server_addr)
        self.assertTrue(s.getpeercert())
        self.assertFalse(s.server_side)
