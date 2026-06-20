# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_connect_with_context_fail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    s = ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname=SIGNED_CERTFILE_HOSTNAME)
    self.addCleanup(s.close)
    self.assertRaisesRegex(ssl.SSLError, 'certificate verify failed', s.connect, self.server_addr)
