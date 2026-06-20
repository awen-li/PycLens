# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: LinuxKernelCryptoAPI_test_length_restriction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket(socket.AF_ALG, socket.SOCK_SEQPACKET, 0)
    self.addCleanup(sock.close)
    with self.assertRaises(FileNotFoundError):
        sock.bind(('t' * 13, 'name'))
    with self.assertRaisesRegex(ValueError, 'type too long'):
        sock.bind(('t' * 14, 'name'))
    with self.assertRaises(FileNotFoundError):
        sock.bind(('type', 'n' * 63))
    with self.assertRaisesRegex(ValueError, 'name too long'):
        sock.bind(('type', 'n' * 64))
