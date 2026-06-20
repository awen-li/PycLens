# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_purpose_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    val = ssl._ASN1Object('1.3.6.1.5.5.7.3.1')
    self.assertIsInstance(ssl.Purpose.SERVER_AUTH, ssl._ASN1Object)
    self.assertEqual(ssl.Purpose.SERVER_AUTH, val)
    self.assertEqual(ssl.Purpose.SERVER_AUTH.nid, 129)
    self.assertEqual(ssl.Purpose.SERVER_AUTH.shortname, 'serverAuth')
    self.assertEqual(ssl.Purpose.SERVER_AUTH.oid, '1.3.6.1.5.5.7.3.1')
    val = ssl._ASN1Object('1.3.6.1.5.5.7.3.2')
    self.assertIsInstance(ssl.Purpose.CLIENT_AUTH, ssl._ASN1Object)
    self.assertEqual(ssl.Purpose.CLIENT_AUTH, val)
    self.assertEqual(ssl.Purpose.CLIENT_AUTH.nid, 130)
    self.assertEqual(ssl.Purpose.CLIENT_AUTH.shortname, 'clientAuth')
    self.assertEqual(ssl.Purpose.CLIENT_AUTH.oid, '1.3.6.1.5.5.7.3.2')
