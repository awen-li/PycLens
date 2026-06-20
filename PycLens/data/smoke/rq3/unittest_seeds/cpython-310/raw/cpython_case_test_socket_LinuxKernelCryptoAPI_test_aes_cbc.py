# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: LinuxKernelCryptoAPI_test_aes_cbc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key = bytes.fromhex('06a9214036b8a15b512e03d534120006')
    iv = bytes.fromhex('3dafba429d9eb430b422da802c9fac41')
    msg = b'Single block msg'
    ciphertext = bytes.fromhex('e353779c1079aeb82708942dbe77181a')
    msglen = len(msg)
    with self.create_alg('skcipher', 'cbc(aes)') as algo:
        algo.setsockopt(socket.SOL_ALG, socket.ALG_SET_KEY, key)
        (op, _) = algo.accept()
        with op:
            op.sendmsg_afalg(op=socket.ALG_OP_ENCRYPT, iv=iv, flags=socket.MSG_MORE)
            op.sendall(msg)
            self.assertEqual(op.recv(msglen), ciphertext)
        (op, _) = algo.accept()
        with op:
            op.sendmsg_afalg([ciphertext], op=socket.ALG_OP_DECRYPT, iv=iv)
            self.assertEqual(op.recv(msglen), msg)
        multiplier = 1024
        longmsg = [msg] * multiplier
        (op, _) = algo.accept()
        with op:
            op.sendmsg_afalg(longmsg, op=socket.ALG_OP_ENCRYPT, iv=iv)
            enc = op.recv(msglen * multiplier)
        self.assertEqual(len(enc), msglen * multiplier)
        self.assertEqual(enc[:msglen], ciphertext)
        (op, _) = algo.accept()
        with op:
            op.sendmsg_afalg([enc], op=socket.ALG_OP_DECRYPT, iv=iv)
            dec = op.recv(msglen * multiplier)
        self.assertEqual(len(dec), msglen * multiplier)
        self.assertEqual(dec, msg * multiplier)
