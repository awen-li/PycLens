# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_sendfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TEST_DATA = b'x' * 512
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(TEST_DATA)
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    (client_context, server_context, hostname) = testing_context()
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            with open(os_helper.TESTFN, 'rb') as file:
                s.sendfile(file)
                self.assertEqual(s.recv(1024), TEST_DATA)
