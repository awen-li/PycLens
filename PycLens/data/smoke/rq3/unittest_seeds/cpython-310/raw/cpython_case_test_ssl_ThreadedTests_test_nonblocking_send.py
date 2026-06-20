# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_nonblocking_send

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = ThreadedEchoServer(CERTFILE, certreqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_TLS_SERVER, cacerts=CERTFILE, chatty=True, connectionchatty=False)
    with server:
        s = test_wrap_socket(socket.socket(), server_side=False, certfile=CERTFILE, ca_certs=CERTFILE, cert_reqs=ssl.CERT_NONE)
        s.connect((HOST, server.port))
        s.setblocking(False)
        buf = bytearray(8192)

        def fill_buffer():
            while True:
                s.send(buf)
        self.assertRaises((ssl.SSLWantWriteError, ssl.SSLWantReadError), fill_buffer)
        s.setblocking(True)
        s.close()
