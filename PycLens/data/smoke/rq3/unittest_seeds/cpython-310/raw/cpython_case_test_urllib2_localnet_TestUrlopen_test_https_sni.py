# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_https_sni

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if ssl is None:
        self.skipTest('ssl module required')
    if not ssl.HAS_SNI:
        self.skipTest('SNI support required in OpenSSL')
    sni_name = None

    def cb_sni(ssl_sock, server_name, initial_context):
        nonlocal sni_name
        sni_name = server_name
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.set_servername_callback(cb_sni)
    handler = self.start_https_server(context=context, certfile=CERT_localhost)
    context = ssl.create_default_context(cafile=CERT_localhost)
    self.urlopen('https://localhost:%s' % handler.port, context=context)
    self.assertEqual(sni_name, 'localhost')
