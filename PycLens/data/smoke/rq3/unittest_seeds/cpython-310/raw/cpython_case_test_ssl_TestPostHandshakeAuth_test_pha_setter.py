# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestPostHandshakeAuth_test_pha_setter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    protocols = [ssl.PROTOCOL_TLS_SERVER, ssl.PROTOCOL_TLS_CLIENT]
    for protocol in protocols:
        ctx = ssl.SSLContext(protocol)
        self.assertEqual(ctx.post_handshake_auth, False)
        ctx.post_handshake_auth = True
        self.assertEqual(ctx.post_handshake_auth, True)
        ctx.verify_mode = ssl.CERT_REQUIRED
        self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
        self.assertEqual(ctx.post_handshake_auth, True)
        ctx.post_handshake_auth = False
        self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
        self.assertEqual(ctx.post_handshake_auth, False)
        ctx.verify_mode = ssl.CERT_OPTIONAL
        ctx.post_handshake_auth = True
        self.assertEqual(ctx.verify_mode, ssl.CERT_OPTIONAL)
        self.assertEqual(ctx.post_handshake_auth, True)
