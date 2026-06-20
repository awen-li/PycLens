# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_cert_store_stats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.cert_store_stats(), {'x509_ca': 0, 'crl': 0, 'x509': 0})
    ctx.load_cert_chain(CERTFILE)
    self.assertEqual(ctx.cert_store_stats(), {'x509_ca': 0, 'crl': 0, 'x509': 0})
    ctx.load_verify_locations(CERTFILE)
    self.assertEqual(ctx.cert_store_stats(), {'x509_ca': 0, 'crl': 0, 'x509': 1})
    ctx.load_verify_locations(CAFILE_CACERT)
    self.assertEqual(ctx.cert_store_stats(), {'x509_ca': 1, 'crl': 0, 'x509': 2})
