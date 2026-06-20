# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_local_good_hostname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import ssl
    server = self.make_server(CERT_localhost)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(CERT_localhost)
    h = client.HTTPSConnection('localhost', server.port, context=context)
    self.addCleanup(h.close)
    h.request('GET', '/nonexistent')
    resp = h.getresponse()
    self.addCleanup(resp.close)
    self.assertEqual(resp.status, 404)
