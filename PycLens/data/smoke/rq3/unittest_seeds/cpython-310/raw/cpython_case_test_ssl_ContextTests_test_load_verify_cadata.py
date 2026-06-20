# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_load_verify_cadata

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(CAFILE_CACERT) as f:
        cacert_pem = f.read()
    cacert_der = ssl.PEM_cert_to_DER_cert(cacert_pem)
    with open(CAFILE_NEURONIO) as f:
        neuronio_pem = f.read()
    neuronio_der = ssl.PEM_cert_to_DER_cert(neuronio_pem)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.cert_store_stats()['x509_ca'], 0)
    ctx.load_verify_locations(cadata=cacert_pem)
    self.assertEqual(ctx.cert_store_stats()['x509_ca'], 1)
    ctx.load_verify_locations(cadata=neuronio_pem)
    self.assertEqual(ctx.cert_store_stats()['x509_ca'], 2)
    ctx.load_verify_locations(cadata=neuronio_pem)
    self.assertEqual(ctx.cert_store_stats()['x509_ca'], 2)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    combined = '\n'.join((cacert_pem, neuronio_pem))
    ctx.load_verify_locations(cadata=combined)
    self.assertEqual(ctx.cert_store_stats()['x509_ca'], 2)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    combined = ['head', cacert_pem, 'other', neuronio_pem, 'again', neuronio_pem, 'tail']
    ctx.load_verify_locations(cadata='\n'.join(combined))
    self.assertEqual(ctx.cert_store_stats()['x509_ca'], 2)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_verify_locations(cadata=cacert_der)
    ctx.load_verify_locations(cadata=neuronio_der)
    self.assertEqual(ctx.cert_store_stats()['x509_ca'], 2)
    ctx.load_verify_locations(cadata=cacert_der)
    self.assertEqual(ctx.cert_store_stats()['x509_ca'], 2)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    combined = b''.join((cacert_der, neuronio_der))
    ctx.load_verify_locations(cadata=combined)
    self.assertEqual(ctx.cert_store_stats()['x509_ca'], 2)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertRaises(TypeError, ctx.load_verify_locations, cadata=object)
    with self.assertRaisesRegex(ssl.SSLError, 'no start line: cadata does not contain a certificate'):
        ctx.load_verify_locations(cadata='broken')
    with self.assertRaisesRegex(ssl.SSLError, 'not enough data: cadata does not contain a certificate'):
        ctx.load_verify_locations(cadata=b'broken')
