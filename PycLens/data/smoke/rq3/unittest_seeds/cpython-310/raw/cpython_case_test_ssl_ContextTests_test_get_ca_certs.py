# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_get_ca_certs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.get_ca_certs(), [])
    ctx.load_verify_locations(CERTFILE)
    self.assertEqual(ctx.get_ca_certs(), [])
    ctx.load_verify_locations(CAFILE_CACERT)
    self.assertEqual(ctx.get_ca_certs(), [{'issuer': ((('organizationName', 'Root CA'),), (('organizationalUnitName', 'http://www.cacert.org'),), (('commonName', 'CA Cert Signing Authority'),), (('emailAddress', 'support@cacert.org'),)), 'notAfter': 'Mar 29 12:29:49 2033 GMT', 'notBefore': 'Mar 30 12:29:49 2003 GMT', 'serialNumber': '00', 'crlDistributionPoints': ('https://www.cacert.org/revoke.crl',), 'subject': ((('organizationName', 'Root CA'),), (('organizationalUnitName', 'http://www.cacert.org'),), (('commonName', 'CA Cert Signing Authority'),), (('emailAddress', 'support@cacert.org'),)), 'version': 3}])
    with open(CAFILE_CACERT) as f:
        pem = f.read()
    der = ssl.PEM_cert_to_DER_cert(pem)
    self.assertEqual(ctx.get_ca_certs(True), [der])
