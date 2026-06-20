# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestSSLDebug_test_msg_callback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()

    def msg_cb(conn, direction, version, content_type, msg_type, data):
        pass
    self.assertIs(client_context._msg_callback, None)
    client_context._msg_callback = msg_cb
    self.assertIs(client_context._msg_callback, msg_cb)
    with self.assertRaises(TypeError):
        client_context._msg_callback = object()
