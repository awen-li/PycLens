# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_ecdh_curve

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    server_context.set_ecdh_curve('secp384r1')
    server_context.set_ciphers('ECDHE:!eNULL:!aNULL')
    server_context.minimum_version = ssl.TLSVersion.TLSv1_2
    stats = server_params_test(client_context, server_context, chatty=True, connectionchatty=True, sni_name=hostname)
    (client_context, server_context, hostname) = testing_context()
    client_context.set_ecdh_curve('secp384r1')
    server_context.set_ciphers('ECDHE:!eNULL:!aNULL')
    server_context.minimum_version = ssl.TLSVersion.TLSv1_2
    stats = server_params_test(client_context, server_context, chatty=True, connectionchatty=True, sni_name=hostname)
    (client_context, server_context, hostname) = testing_context()
    client_context.set_ecdh_curve('prime256v1')
    server_context.set_ecdh_curve('secp384r1')
    server_context.set_ciphers('ECDHE:!eNULL:!aNULL')
    server_context.minimum_version = ssl.TLSVersion.TLSv1_2
    with self.assertRaises(ssl.SSLError):
        server_params_test(client_context, server_context, chatty=True, connectionchatty=True, sni_name=hostname)
