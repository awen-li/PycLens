# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_https

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = self.start_https_server()
    context = ssl.create_default_context(cafile=CERT_localhost)
    data = self.urlopen('https://localhost:%s/bizarre' % handler.port, context=context)
    self.assertEqual(data, b'we care a bit')
