# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_host_port

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for hp in ('www.python.org:abc', 'user:password@www.python.org'):
        self.assertRaises(client.InvalidURL, client.HTTPSConnection, hp)
    for (hp, h, p) in (('[fe80::207:e9ff:fe9b]:8000', 'fe80::207:e9ff:fe9b', 8000), ('www.python.org:443', 'www.python.org', 443), ('www.python.org:', 'www.python.org', 443), ('www.python.org', 'www.python.org', 443), ('[fe80::207:e9ff:fe9b]', 'fe80::207:e9ff:fe9b', 443), ('[fe80::207:e9ff:fe9b]:', 'fe80::207:e9ff:fe9b', 443)):
        c = client.HTTPSConnection(hp)
        self.assertEqual(h, c.host)
        self.assertEqual(p, c.port)
