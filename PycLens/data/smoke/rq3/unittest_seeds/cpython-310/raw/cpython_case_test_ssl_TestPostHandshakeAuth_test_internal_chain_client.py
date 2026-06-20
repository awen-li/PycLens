# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestPostHandshakeAuth_test_internal_chain_client

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context(server_chain=False)
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            vc = s._sslobj.get_verified_chain()
            self.assertEqual(len(vc), 2)
            (ee, ca) = vc
            uvc = s._sslobj.get_unverified_chain()
            self.assertEqual(len(uvc), 1)
            self.assertEqual(ee, uvc[0])
            self.assertEqual(hash(ee), hash(uvc[0]))
            self.assertEqual(repr(ee), repr(uvc[0]))
            self.assertNotEqual(ee, ca)
            self.assertNotEqual(hash(ee), hash(ca))
            self.assertNotEqual(repr(ee), repr(ca))
            self.assertNotEqual(ee.get_info(), ca.get_info())
            self.assertIn('CN=localhost', repr(ee))
            self.assertIn('CN=our-ca-server', repr(ca))
            pem = ee.public_bytes(_ssl.ENCODING_PEM)
            der = ee.public_bytes(_ssl.ENCODING_DER)
            self.assertIsInstance(pem, str)
            self.assertIn('-----BEGIN CERTIFICATE-----', pem)
            self.assertIsInstance(der, bytes)
            self.assertEqual(ssl.PEM_cert_to_DER_cert(pem), der)
