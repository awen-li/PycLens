# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestSSLDebug_test_keylog_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    (client_context, server_context, hostname) = testing_context()
    client_context.keylog_filename = os_helper.TESTFN
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
    self.assertEqual(self.keylog_lines(), 6)
    client_context.keylog_filename = None
    server_context.keylog_filename = os_helper.TESTFN
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
    self.assertGreaterEqual(self.keylog_lines(), 11)
    client_context.keylog_filename = os_helper.TESTFN
    server_context.keylog_filename = os_helper.TESTFN
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
    self.assertGreaterEqual(self.keylog_lines(), 21)
    client_context.keylog_filename = None
    server_context.keylog_filename = None
