# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_alpn_protocols

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server_protocols = ['foo', 'bar', 'milkshake']
    protocol_tests = [(['foo', 'bar'], 'foo'), (['bar', 'foo'], 'foo'), (['milkshake'], 'milkshake'), (['http/3.0', 'http/4.0'], None)]
    for (client_protocols, expected) in protocol_tests:
        (client_context, server_context, hostname) = testing_context()
        server_context.set_alpn_protocols(server_protocols)
        client_context.set_alpn_protocols(client_protocols)
        try:
            stats = server_params_test(client_context, server_context, chatty=True, connectionchatty=True, sni_name=hostname)
        except ssl.SSLError as e:
            stats = e
        msg = 'failed trying %s (s) and %s (c).\nwas expecting %s, but got %%s from the %%s' % (str(server_protocols), str(client_protocols), str(expected))
        client_result = stats['client_alpn_protocol']
        self.assertEqual(client_result, expected, msg % (client_result, 'client'))
        server_result = stats['server_alpn_protocols'][-1] if len(stats['server_alpn_protocols']) else 'nothing'
        self.assertEqual(server_result, expected, msg % (server_result, 'server'))
