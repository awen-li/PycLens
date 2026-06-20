# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_transport_eof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    with socket.socket(socket.AF_INET) as sock:
        sock.connect(self.server_addr)
        incoming = ssl.MemoryBIO()
        outgoing = ssl.MemoryBIO()
        sslobj = client_context.wrap_bio(incoming, outgoing, server_hostname=hostname)
        self.ssl_io_loop(sock, incoming, outgoing, sslobj.do_handshake)
        incoming.write_eof()
        self.assertRaises(ssl.SSLEOFError, sslobj.read)
