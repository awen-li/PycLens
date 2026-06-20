# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_parse_cert_CVE_2019_5010

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = ssl._ssl._test_decode_cert(TALOS_INVALID_CRLDP)
    if support.verbose:
        sys.stdout.write('\n' + pprint.pformat(p) + '\n')
    self.assertEqual(p, {'issuer': ((('countryName', 'UK'),), (('commonName', 'cody-ca'),)), 'notAfter': 'Jun 14 18:00:58 2028 GMT', 'notBefore': 'Jun 18 18:00:58 2018 GMT', 'serialNumber': '02', 'subject': ((('countryName', 'UK'),), (('commonName', 'codenomicon-vm-2.test.lal.cisco.com'),)), 'subjectAltName': (('DNS', 'codenomicon-vm-2.test.lal.cisco.com'),), 'version': 3})
