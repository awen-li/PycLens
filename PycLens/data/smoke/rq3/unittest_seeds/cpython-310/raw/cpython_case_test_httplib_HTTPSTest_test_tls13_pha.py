# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_tls13_pha

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import ssl
    if not ssl.HAS_TLSv1_3:
        self.skipTest('TLS 1.3 support required')
    h = client.HTTPSConnection('localhost', 443)
    self.assertTrue(h._context.post_handshake_auth)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertFalse(context.post_handshake_auth)
    h = client.HTTPSConnection('localhost', 443, context=context)
    self.assertIs(h._context, context)
    self.assertFalse(h._context.post_handshake_auth)
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', 'key_file, cert_file and check_hostname are deprecated', DeprecationWarning)
        h = client.HTTPSConnection('localhost', 443, context=context, cert_file=CERT_localhost)
    self.assertTrue(h._context.post_handshake_auth)
