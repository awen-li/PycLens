# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_unsupported_dtls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.addCleanup(s.close)
    with self.assertRaises(NotImplementedError) as cx:
        test_wrap_socket(s, cert_reqs=ssl.CERT_NONE)
    self.assertEqual(str(cx.exception), 'only stream sockets are supported')
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    with self.assertRaises(NotImplementedError) as cx:
        ctx.wrap_socket(s)
    self.assertEqual(str(cx.exception), 'only stream sockets are supported')
