# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: LinuxKernelCryptoAPI_test_sha256

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = bytes.fromhex('ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')
    with self.create_alg('hash', 'sha256') as algo:
        (op, _) = algo.accept()
        with op:
            op.sendall(b'abc')
            self.assertEqual(op.recv(512), expected)
        (op, _) = algo.accept()
        with op:
            op.send(b'a', socket.MSG_MORE)
            op.send(b'b', socket.MSG_MORE)
            op.send(b'c', socket.MSG_MORE)
            op.send(b'')
            self.assertEqual(op.recv(512), expected)
