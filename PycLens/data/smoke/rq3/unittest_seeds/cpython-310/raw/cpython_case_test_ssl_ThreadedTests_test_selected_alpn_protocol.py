# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_selected_alpn_protocol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    stats = server_params_test(client_context, server_context, chatty=True, connectionchatty=True, sni_name=hostname)
    self.assertIs(stats['client_alpn_protocol'], None)
