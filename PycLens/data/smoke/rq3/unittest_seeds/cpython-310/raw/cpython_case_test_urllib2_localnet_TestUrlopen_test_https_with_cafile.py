# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_https_with_cafile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = self.start_https_server(certfile=CERT_localhost)
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        data = self.urlopen('https://localhost:%s/bizarre' % handler.port, cafile=CERT_localhost)
        self.assertEqual(data, b'we care a bit')
        with self.assertRaises(urllib.error.URLError) as cm:
            self.urlopen('https://localhost:%s/bizarre' % handler.port, cafile=CERT_fakehostname)
        handler = self.start_https_server(certfile=CERT_fakehostname)
        with self.assertRaises(urllib.error.URLError) as cm:
            self.urlopen('https://localhost:%s/bizarre' % handler.port, cafile=CERT_fakehostname)
