# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_parse_cert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ssl._ssl._test_decode_cert(CERTFILE), CERTFILE_INFO)
    self.assertEqual(ssl._ssl._test_decode_cert(SIGNED_CERTFILE), SIGNED_CERTFILE_INFO)
    p = ssl._ssl._test_decode_cert(NOKIACERT)
    if support.verbose:
        sys.stdout.write('\n' + pprint.pformat(p) + '\n')
    self.assertEqual(p['subjectAltName'], (('DNS', 'projects.developer.nokia.com'), ('DNS', 'projects.forum.nokia.com')))
    self.assertEqual(p['OCSP'], ('http://ocsp.verisign.com',))
    self.assertEqual(p['caIssuers'], ('http://SVRIntl-G3-aia.verisign.com/SVRIntlG3.cer',))
    self.assertEqual(p['crlDistributionPoints'], ('http://SVRIntl-G3-crl.verisign.com/SVRIntlG3.crl',))
