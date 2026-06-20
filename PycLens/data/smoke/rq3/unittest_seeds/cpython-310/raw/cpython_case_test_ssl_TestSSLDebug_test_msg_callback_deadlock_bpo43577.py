# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestSSLDebug_test_msg_callback_deadlock_bpo43577

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    server_context2 = testing_context()[1]

    def msg_cb(conn, direction, version, content_type, msg_type, data):
        pass

    def sni_cb(sock, servername, ctx):
        sock.context = server_context2
    server_context._msg_callback = msg_cb
    server_context.sni_callback = sni_cb
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
