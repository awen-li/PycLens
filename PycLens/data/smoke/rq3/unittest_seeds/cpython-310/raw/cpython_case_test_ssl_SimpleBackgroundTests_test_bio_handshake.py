# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_bio_handshake

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket(socket.AF_INET)
    self.addCleanup(sock.close)
    sock.connect(self.server_addr)
    incoming = ssl.MemoryBIO()
    outgoing = ssl.MemoryBIO()
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertTrue(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    ctx.load_verify_locations(SIGNING_CA)
    sslobj = ctx.wrap_bio(incoming, outgoing, False, SIGNED_CERTFILE_HOSTNAME)
    self.assertIs(sslobj._sslobj.owner, sslobj)
    self.assertIsNone(sslobj.cipher())
    self.assertIsNone(sslobj.version())
    self.assertIsNone(sslobj.shared_ciphers())
    self.assertRaises(ValueError, sslobj.getpeercert)
    if 'tls-unique' in ssl.CHANNEL_BINDING_TYPES:
        self.assertIsNone(sslobj.get_channel_binding('tls-unique'))
    self.ssl_io_loop(sock, incoming, outgoing, sslobj.do_handshake)
    self.assertTrue(sslobj.cipher())
    self.assertIsNone(sslobj.shared_ciphers())
    self.assertIsNotNone(sslobj.version())
    self.assertTrue(sslobj.getpeercert())
    if 'tls-unique' in ssl.CHANNEL_BINDING_TYPES:
        self.assertTrue(sslobj.get_channel_binding('tls-unique'))
    try:
        self.ssl_io_loop(sock, incoming, outgoing, sslobj.unwrap)
    except ssl.SSLSyscallError:
        pass
    self.assertRaises(ssl.SSLError, sslobj.write, b'foo')
