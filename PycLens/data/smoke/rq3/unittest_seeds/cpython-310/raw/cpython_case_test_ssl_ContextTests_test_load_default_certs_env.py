# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_load_default_certs_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    with os_helper.EnvironmentVarGuard() as env:
        env['SSL_CERT_DIR'] = CAPATH
        env['SSL_CERT_FILE'] = CERTFILE
        ctx.load_default_certs()
        self.assertEqual(ctx.cert_store_stats(), {'crl': 0, 'x509': 1, 'x509_ca': 0})
