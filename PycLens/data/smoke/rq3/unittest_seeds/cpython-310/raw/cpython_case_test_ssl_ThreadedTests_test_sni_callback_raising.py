# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_sni_callback_raising

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (server_context, other_context, client_context) = self.sni_contexts()

    def cb_raising(ssl_sock, server_name, initial_context):
        1 / 0
    server_context.set_servername_callback(cb_raising)
    with support.catch_unraisable_exception() as catch:
        with self.assertRaises(ssl.SSLError) as cm:
            stats = server_params_test(client_context, server_context, chatty=False, sni_name='supermessage')
        self.assertEqual(cm.exception.reason, 'SSLV3_ALERT_HANDSHAKE_FAILURE')
        self.assertEqual(catch.unraisable.exc_type, ZeroDivisionError)
