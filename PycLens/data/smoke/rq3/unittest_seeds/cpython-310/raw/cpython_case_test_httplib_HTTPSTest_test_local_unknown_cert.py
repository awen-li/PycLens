# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_local_unknown_cert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import ssl
    server = self.make_server(CERT_localhost)
    h = client.HTTPSConnection('localhost', server.port)
    with self.assertRaises(ssl.SSLError) as exc_info:
        h.request('GET', '/')
    self.assertEqual(exc_info.exception.reason, 'CERTIFICATE_VERIFY_FAILED')
