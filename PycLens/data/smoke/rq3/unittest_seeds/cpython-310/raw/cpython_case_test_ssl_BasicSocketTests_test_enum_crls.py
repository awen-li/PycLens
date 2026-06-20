# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_enum_crls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(ssl.enum_crls('CA'))
    self.assertRaises(TypeError, ssl.enum_crls)
    self.assertRaises(WindowsError, ssl.enum_crls, '')
    crls = ssl.enum_crls('CA')
    self.assertIsInstance(crls, list)
    for element in crls:
        self.assertIsInstance(element, tuple)
        self.assertEqual(len(element), 2)
        self.assertIsInstance(element[0], bytes)
        self.assertIn(element[1], {'x509_asn', 'pkcs_7_asn'})
