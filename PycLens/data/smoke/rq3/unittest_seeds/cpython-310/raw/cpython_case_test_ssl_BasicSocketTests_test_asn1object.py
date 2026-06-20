# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_asn1object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = (129, 'serverAuth', 'TLS Web Server Authentication', '1.3.6.1.5.5.7.3.1')
    val = ssl._ASN1Object('1.3.6.1.5.5.7.3.1')
    self.assertEqual(val, expected)
    self.assertEqual(val.nid, 129)
    self.assertEqual(val.shortname, 'serverAuth')
    self.assertEqual(val.longname, 'TLS Web Server Authentication')
    self.assertEqual(val.oid, '1.3.6.1.5.5.7.3.1')
    self.assertIsInstance(val, ssl._ASN1Object)
    self.assertRaises(ValueError, ssl._ASN1Object, 'serverAuth')
    val = ssl._ASN1Object.fromnid(129)
    self.assertEqual(val, expected)
    self.assertIsInstance(val, ssl._ASN1Object)
    self.assertRaises(ValueError, ssl._ASN1Object.fromnid, -1)
    with self.assertRaisesRegex(ValueError, 'unknown NID 100000'):
        ssl._ASN1Object.fromnid(100000)
    for i in range(1000):
        try:
            obj = ssl._ASN1Object.fromnid(i)
        except ValueError:
            pass
        else:
            self.assertIsInstance(obj.nid, int)
            self.assertIsInstance(obj.shortname, str)
            self.assertIsInstance(obj.longname, str)
            self.assertIsInstance(obj.oid, (str, type(None)))
    val = ssl._ASN1Object.fromname('TLS Web Server Authentication')
    self.assertEqual(val, expected)
    self.assertIsInstance(val, ssl._ASN1Object)
    self.assertEqual(ssl._ASN1Object.fromname('serverAuth'), expected)
    self.assertEqual(ssl._ASN1Object.fromname('1.3.6.1.5.5.7.3.1'), expected)
    with self.assertRaisesRegex(ValueError, "unknown object 'serverauth'"):
        ssl._ASN1Object.fromname('serverauth')
