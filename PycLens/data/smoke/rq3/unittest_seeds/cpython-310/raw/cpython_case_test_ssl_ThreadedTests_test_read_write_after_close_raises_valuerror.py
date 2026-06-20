# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_read_write_after_close_raises_valuerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        s = client_context.wrap_socket(socket.socket(), server_hostname=hostname)
        s.connect((HOST, server.port))
        s.close()
        self.assertRaises(ValueError, s.read, 1024)
        self.assertRaises(ValueError, s.write, b'hello')
