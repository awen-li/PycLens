# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_bio_read_write_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket(socket.AF_INET)
    self.addCleanup(sock.close)
    sock.connect(self.server_addr)
    incoming = ssl.MemoryBIO()
    outgoing = ssl.MemoryBIO()
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    sslobj = ctx.wrap_bio(incoming, outgoing, False)
    self.ssl_io_loop(sock, incoming, outgoing, sslobj.do_handshake)
    req = b'FOO\n'
    self.ssl_io_loop(sock, incoming, outgoing, sslobj.write, req)
    buf = self.ssl_io_loop(sock, incoming, outgoing, sslobj.read, 1024)
    self.assertEqual(buf, b'foo\n')
    self.ssl_io_loop(sock, incoming, outgoing, sslobj.unwrap)
