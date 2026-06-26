# Source Generated with Decompyle++
# File: cpython-312-57e84b72505f.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.get_ca_certs(), [])
    ctx.load_verify_locations(CERTFILE)
    self.assertEqual(ctx.get_ca_certs(), [])
    ctx.load_verify_locations(CAFILE_CACERT)
    self.assertEqual(ctx.get_ca_certs(), [
        {
            'issuer': ((('organizationName', 'Root CA'),), (('organizationalUnitName', 'http://www.cacert.org'),), (('commonName', 'CA Cert Signing Authority'),), (('emailAddress', 'support@cacert.org'),)),
            'notAfter': 'Mar 29 12:29:49 2033 GMT',
            'notBefore': 'Mar 30 12:29:49 2003 GMT',
            'serialNumber': '00',
            'crlDistributionPoints': ('https://www.cacert.org/revoke.crl',),
            'subject': ((('organizationName', 'Root CA'),), (('organizationalUnitName', 'http://www.cacert.org'),), (('commonName', 'CA Cert Signing Authority'),), (('emailAddress', 'support@cacert.org'),)),
            'version': 3 }])
    f = open(CAFILE_CACERT)
    pem = f.read()
    None(None, None)
    der = None(ssl.PEM_cert_to_DER_cert)
    self.assertEqual(ctx.get_ca_certs(True), [
        der])
    return None
    if None:
        pass
    with None:
        if not None:
            pass
    continue

None.__name__ = None
if None == '__main__':
    __pybcsec_seed__()
    return None
