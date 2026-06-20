# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_networked_good_cert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import ssl
    support.requires('network')
    selfsigned_pythontestdotnet = 'self-signed.pythontest.net'
    with socket_helper.transient_internet(selfsigned_pythontestdotnet):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)
        self.assertEqual(context.check_hostname, True)
        context.load_verify_locations(CERT_selfsigned_pythontestdotnet)
        try:
            h = client.HTTPSConnection(selfsigned_pythontestdotnet, 443, context=context)
            h.request('GET', '/')
            resp = h.getresponse()
        except ssl.SSLError as ssl_err:
            ssl_err_str = str(ssl_err)
            if re.search('(?i)key.too.weak', ssl_err_str):
                raise unittest.SkipTest(f'Got {ssl_err_str} trying to connect to {selfsigned_pythontestdotnet}. See https://bugs.python.org/issue36816.')
            raise
        server_string = resp.getheader('server')
        resp.close()
        h.close()
        self.assertIn('nginx', server_string)
