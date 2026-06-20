# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_parse_cert_CVE_2013_4238

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = ssl._ssl._test_decode_cert(NULLBYTECERT)
    if support.verbose:
        sys.stdout.write('\n' + pprint.pformat(p) + '\n')
    subject = ((('countryName', 'US'),), (('stateOrProvinceName', 'Oregon'),), (('localityName', 'Beaverton'),), (('organizationName', 'Python Software Foundation'),), (('organizationalUnitName', 'Python Core Development'),), (('commonName', 'null.python.org\x00example.org'),), (('emailAddress', 'python-dev@python.org'),))
    self.assertEqual(p['subject'], subject)
    self.assertEqual(p['issuer'], subject)
    if ssl._OPENSSL_API_VERSION >= (0, 9, 8):
        san = (('DNS', 'altnull.python.org\x00example.com'), ('email', 'null@python.org\x00user@example.org'), ('URI', 'http://null.python.org\x00http://example.org'), ('IP Address', '192.0.2.1'), ('IP Address', '2001:DB8:0:0:0:0:0:1'))
    else:
        san = (('DNS', 'altnull.python.org\x00example.com'), ('email', 'null@python.org\x00user@example.org'), ('URI', 'http://null.python.org\x00http://example.org'), ('IP Address', '192.0.2.1'), ('IP Address', '<invalid>'))
    self.assertEqual(p['subjectAltName'], san)
