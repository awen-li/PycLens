# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_getpeercert_enotconn

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    with context.wrap_socket(socket.socket()) as sock:
        with self.assertRaises(OSError) as cm:
            sock.getpeercert()
        self.assertEqual(cm.exception.errno, errno.ENOTCONN)
