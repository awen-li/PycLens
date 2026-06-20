# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_connect_with_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with ctx.wrap_socket(socket.socket(socket.AF_INET)) as s:
        s.connect(self.server_addr)
        self.assertEqual({}, s.getpeercert())
    with ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname='dummy') as s:
        s.connect(self.server_addr)
    ctx.verify_mode = ssl.CERT_REQUIRED
    ctx.load_verify_locations(SIGNING_CA)
    with ctx.wrap_socket(socket.socket(socket.AF_INET)) as s:
        s.connect(self.server_addr)
        cert = s.getpeercert()
        self.assertTrue(cert)
