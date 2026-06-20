# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: LinuxKernelCryptoAPI_test_hmac_sha1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = bytes.fromhex('effcdf6ae5eb2fa2d27416d5f184df9c259a7c79')
    with self.create_alg('hash', 'hmac(sha1)') as algo:
        algo.setsockopt(socket.SOL_ALG, socket.ALG_SET_KEY, b'Jefe')
        (op, _) = algo.accept()
        with op:
            op.sendall(b'what do ya want for nothing?')
            self.assertEqual(op.recv(512), expected)
