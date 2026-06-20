# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_shared_ciphers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    client_context.set_ciphers('AES128:AES256')
    server_context.set_ciphers('AES256:eNULL')
    expected_algs = ['AES256', 'AES-256', 'TLS_CHACHA20', 'TLS_AES']
    stats = server_params_test(client_context, server_context, sni_name=hostname)
    ciphers = stats['server_shared_ciphers'][0]
    self.assertGreater(len(ciphers), 0)
    for (name, tls_version, bits) in ciphers:
        if not any((alg in name for alg in expected_algs)):
            self.fail(name)
