# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_enum_certificates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(ssl.enum_certificates('CA'))
    self.assertTrue(ssl.enum_certificates('ROOT'))
    self.assertRaises(TypeError, ssl.enum_certificates)
    self.assertRaises(WindowsError, ssl.enum_certificates, '')
    trust_oids = set()
    for storename in ('CA', 'ROOT'):
        store = ssl.enum_certificates(storename)
        self.assertIsInstance(store, list)
        for element in store:
            self.assertIsInstance(element, tuple)
            self.assertEqual(len(element), 3)
            (cert, enc, trust) = element
            self.assertIsInstance(cert, bytes)
            self.assertIn(enc, {'x509_asn', 'pkcs_7_asn'})
            self.assertIsInstance(trust, (frozenset, set, bool))
            if isinstance(trust, (frozenset, set)):
                trust_oids.update(trust)
    serverAuth = '1.3.6.1.5.5.7.3.1'
    self.assertIn(serverAuth, trust_oids)
