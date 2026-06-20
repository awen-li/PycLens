# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_compression_disabled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    client_context.options |= ssl.OP_NO_COMPRESSION
    server_context.options |= ssl.OP_NO_COMPRESSION
    stats = server_params_test(client_context, server_context, chatty=True, connectionchatty=True, sni_name=hostname)
    self.assertIs(stats['compression'], None)
