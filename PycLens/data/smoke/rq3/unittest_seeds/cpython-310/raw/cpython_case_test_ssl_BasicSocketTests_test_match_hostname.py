# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_match_hostname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def ok(cert, hostname):
        ssl.match_hostname(cert, hostname)

    def fail(cert, hostname):
        self.assertRaises(ssl.CertificateError, ssl.match_hostname, cert, hostname)
    cert = {'subject': ((('commonName', 'example.com'),),)}
    ok(cert, 'example.com')
    ok(cert, 'ExAmple.cOm')
    fail(cert, 'www.example.com')
    fail(cert, '.example.com')
    fail(cert, 'example.org')
    fail(cert, 'exampleXcom')
    cert = {'subject': ((('commonName', '*.a.com'),),)}
    ok(cert, 'foo.a.com')
    fail(cert, 'bar.foo.a.com')
    fail(cert, 'a.com')
    fail(cert, 'Xa.com')
    fail(cert, '.a.com')
    cert = {'subject': ((('commonName', 'f*.com'),),)}
    fail(cert, 'foo.com')
    fail(cert, 'f.com')
    fail(cert, 'bar.com')
    fail(cert, 'foo.a.com')
    fail(cert, 'bar.foo.com')
    cert = {'subject': ((('commonName', 'null.python.org\x00example.org'),),)}
    ok(cert, 'null.python.org\x00example.org')
    fail(cert, 'example.org')
    fail(cert, 'null.python.org')
    cert = {'subject': ((('commonName', '*.*.a.com'),),)}
    fail(cert, 'bar.foo.a.com')
    fail(cert, 'a.com')
    fail(cert, 'Xa.com')
    fail(cert, '.a.com')
    cert = {'subject': ((('commonName', 'a.*.com'),),)}
    fail(cert, 'a.foo.com')
    fail(cert, 'a..com')
    fail(cert, 'a.com')
    idna = 'püthon.python.org'.encode('idna').decode('ascii')
    cert = {'subject': ((('commonName', idna),),)}
    ok(cert, idna)
    cert = {'subject': ((('commonName', 'x*.python.org'),),)}
    fail(cert, idna)
    cert = {'subject': ((('commonName', 'xn--p*.python.org'),),)}
    fail(cert, idna)
    idna = 'www*.pythön.org'.encode('idna').decode('ascii')
    cert = {'subject': ((('commonName', idna),),)}
    fail(cert, 'www.pythön.org'.encode('idna').decode('ascii'))
    fail(cert, 'www1.pythön.org'.encode('idna').decode('ascii'))
    fail(cert, 'ftp.pythön.org'.encode('idna').decode('ascii'))
    fail(cert, 'pythön.org'.encode('idna').decode('ascii'))
    cert = {'notAfter': 'Jun 26 21:41:46 2011 GMT', 'subject': ((('commonName', 'linuxfrz.org'),),), 'subjectAltName': (('DNS', 'linuxfr.org'), ('DNS', 'linuxfr.com'), ('othername', '<unsupported>'))}
    ok(cert, 'linuxfr.org')
    ok(cert, 'linuxfr.com')
    fail(cert, '<unsupported>')
    fail(cert, 'linuxfrz.org')
    cert = {'notAfter': 'Dec 18 23:59:59 2011 GMT', 'subject': ((('countryName', 'US'),), (('stateOrProvinceName', 'California'),), (('localityName', 'Mountain View'),), (('organizationName', 'Google Inc'),), (('commonName', 'mail.google.com'),))}
    ok(cert, 'mail.google.com')
    fail(cert, 'gmail.com')
    fail(cert, 'California')
    cert = {'subject': ((('commonName', 'example.com'),),), 'subjectAltName': (('DNS', 'example.com'), ('IP Address', '10.11.12.13'), ('IP Address', '14.15.16.17'), ('IP Address', '127.0.0.1'))}
    ok(cert, '10.11.12.13')
    ok(cert, '14.15.16.17')
    fail(cert, '127.1')
    fail(cert, '14.15.16.17 ')
    fail(cert, '14.15.16.17 extra data')
    fail(cert, '14.15.16.18')
    fail(cert, 'example.net')
    if socket_helper.IPV6_ENABLED:
        cert = {'subject': ((('commonName', 'example.com'),),), 'subjectAltName': (('DNS', 'example.com'), ('IP Address', '2001:0:0:0:0:0:0:CAFE\n'), ('IP Address', '2003:0:0:0:0:0:0:BABA\n'))}
        ok(cert, '2001::cafe')
        ok(cert, '2003::baba')
        fail(cert, '2003::baba ')
        fail(cert, '2003::baba extra data')
        fail(cert, '2003::bebe')
        fail(cert, 'example.net')
    cert = {'notAfter': 'Dec 18 23:59:59 2011 GMT', 'subject': ((('countryName', 'US'),), (('stateOrProvinceName', 'California'),), (('localityName', 'Mountain View'),), (('organizationName', 'Google Inc'),))}
    fail(cert, 'mail.google.com')
    cert = {'notAfter': 'Dec 18 23:59:59 2099 GMT', 'subject': ((('countryName', 'US'),), (('stateOrProvinceName', 'California'),), (('localityName', 'Mountain View'),), (('commonName', 'mail.google.com'),)), 'subjectAltName': (('othername', 'blabla'),)}
    ok(cert, 'mail.google.com')
    cert = {'notAfter': 'Dec 18 23:59:59 2099 GMT', 'subject': ((('countryName', 'US'),), (('stateOrProvinceName', 'California'),), (('localityName', 'Mountain View'),), (('organizationName', 'Google Inc'),)), 'subjectAltName': (('othername', 'blabla'),)}
    fail(cert, 'google.com')
    self.assertRaises(ValueError, ssl.match_hostname, None, 'example.com')
    self.assertRaises(ValueError, ssl.match_hostname, {}, 'example.com')
    cert = {'subject': ((('commonName', 'a*b.example.com'),),)}
    with self.assertRaisesRegex(ssl.CertificateError, 'partial wildcards in leftmost label are not supported'):
        ssl.match_hostname(cert, 'axxb.example.com')
    cert = {'subject': ((('commonName', 'www.*.example.com'),),)}
    with self.assertRaisesRegex(ssl.CertificateError, 'wildcard can only be present in the leftmost label'):
        ssl.match_hostname(cert, 'www.sub.example.com')
    cert = {'subject': ((('commonName', 'a*b*.example.com'),),)}
    with self.assertRaisesRegex(ssl.CertificateError, 'too many wildcards'):
        ssl.match_hostname(cert, 'axxbxxc.example.com')
    cert = {'subject': ((('commonName', '*'),),)}
    with self.assertRaisesRegex(ssl.CertificateError, 'sole wildcard without additional labels are not support'):
        ssl.match_hostname(cert, 'host')
    cert = {'subject': ((('commonName', '*.com'),),)}
    with self.assertRaisesRegex(ssl.CertificateError, "hostname 'com' doesn't match '\\*.com'"):
        ssl.match_hostname(cert, 'com')
    for invalid in ['1', '', '1.2.3', '256.0.0.1', '127.0.0.1/24']:
        with self.assertRaises(ValueError):
            ssl._inet_paton(invalid)
    for ipaddr in ['127.0.0.1', '192.168.0.1']:
        self.assertTrue(ssl._inet_paton(ipaddr))
    if socket_helper.IPV6_ENABLED:
        for ipaddr in ['::1', '2001:db8:85a3::8a2e:370:7334']:
            self.assertTrue(ssl._inet_paton(ipaddr))
