# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_local_bad_hostname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import ssl
    server = self.make_server(CERT_fakehostname)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(CERT_fakehostname)
    h = client.HTTPSConnection('localhost', server.port, context=context)
    with self.assertRaises(ssl.CertificateError):
        h.request('GET', '/')
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        h = client.HTTPSConnection('localhost', server.port, context=context, check_hostname=True)
    with self.assertRaises(ssl.CertificateError):
        h.request('GET', '/')
    context.check_hostname = False
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        h = client.HTTPSConnection('localhost', server.port, context=context, check_hostname=False)
    h.request('GET', '/nonexistent')
    resp = h.getresponse()
    resp.close()
    h.close()
    self.assertEqual(resp.status, 404)
    context.check_hostname = False
    h = client.HTTPSConnection('localhost', server.port, context=context)
    h.request('GET', '/nonexistent')
    resp = h.getresponse()
    self.assertEqual(resp.status, 404)
    resp.close()
    h.close()
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        h = client.HTTPSConnection('localhost', server.port, context=context, check_hostname=True)
    with self.assertRaises(ssl.CertificateError):
        h.request('GET', '/')
