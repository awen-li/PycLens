# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_connect_capath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_verify_locations(capath=CAPATH)
    with ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname=SIGNED_CERTFILE_HOSTNAME) as s:
        s.connect(self.server_addr)
        cert = s.getpeercert()
        self.assertTrue(cert)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_verify_locations(capath=BYTES_CAPATH)
    with ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname=SIGNED_CERTFILE_HOSTNAME) as s:
        s.connect(self.server_addr)
        cert = s.getpeercert()
        self.assertTrue(cert)
