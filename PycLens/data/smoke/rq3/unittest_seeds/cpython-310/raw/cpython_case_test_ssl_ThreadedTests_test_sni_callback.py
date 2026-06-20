# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_sni_callback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    calls = []
    (server_context, other_context, client_context) = self.sni_contexts()
    client_context.check_hostname = False

    def servername_cb(ssl_sock, server_name, initial_context):
        calls.append((server_name, initial_context))
        if server_name is not None:
            ssl_sock.context = other_context
    server_context.set_servername_callback(servername_cb)
    stats = server_params_test(client_context, server_context, chatty=True, sni_name='supermessage')
    self.assertEqual(calls, [('supermessage', server_context)])
    self.check_common_name(stats, 'fakehostname')
    calls = []
    stats = server_params_test(client_context, server_context, chatty=True, sni_name=None)
    self.assertEqual(calls, [(None, server_context)])
    self.check_common_name(stats, SIGNED_CERTFILE_HOSTNAME)
    calls = []
    server_context.set_servername_callback(None)
    stats = server_params_test(client_context, server_context, chatty=True, sni_name='notfunny')
    self.check_common_name(stats, SIGNED_CERTFILE_HOSTNAME)
    self.assertEqual(calls, [])
