# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_networked_bad_cert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import ssl
    support.requires('network')
    with socket_helper.transient_internet('self-signed.pythontest.net'):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.load_verify_locations(CERT_localhost)
        h = client.HTTPSConnection('self-signed.pythontest.net', 443, context=context)
        with self.assertRaises(ssl.SSLError) as exc_info:
            h.request('GET', '/')
        self.assertEqual(exc_info.exception.reason, 'CERTIFICATE_VERIFY_FAILED')
