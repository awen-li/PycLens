# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: LinuxKernelCryptoAPI_test_aead_aes_gcm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key = bytes.fromhex('c939cc13397c1d37de6ae0e1cb7c423c')
    iv = bytes.fromhex('b3d8cc017cbb89b39e0f67e2')
    plain = bytes.fromhex('c3b3c41f113a31b73d9a5cd432103069')
    assoc = bytes.fromhex('24825602bd12a984e0092d3e448eda5f')
    expected_ct = bytes.fromhex('93fe7d9e9bfd10348a5606e5cafa7354')
    expected_tag = bytes.fromhex('0032a1dc85f1c9786925a2e71d8272dd')
    taglen = len(expected_tag)
    assoclen = len(assoc)
    with self.create_alg('aead', 'gcm(aes)') as algo:
        algo.setsockopt(socket.SOL_ALG, socket.ALG_SET_KEY, key)
        algo.setsockopt(socket.SOL_ALG, socket.ALG_SET_AEAD_AUTHSIZE, None, taglen)
        (op, _) = algo.accept()
        with op:
            op.sendmsg_afalg(op=socket.ALG_OP_ENCRYPT, iv=iv, assoclen=assoclen, flags=socket.MSG_MORE)
            op.sendall(assoc, socket.MSG_MORE)
            op.sendall(plain)
            res = op.recv(assoclen + len(plain) + taglen)
            self.assertEqual(expected_ct, res[assoclen:-taglen])
            self.assertEqual(expected_tag, res[-taglen:])
        (op, _) = algo.accept()
        with op:
            msg = assoc + plain
            op.sendmsg_afalg([msg], op=socket.ALG_OP_ENCRYPT, iv=iv, assoclen=assoclen)
            res = op.recv(assoclen + len(plain) + taglen)
            self.assertEqual(expected_ct, res[assoclen:-taglen])
            self.assertEqual(expected_tag, res[-taglen:])
        pack_uint32 = struct.Struct('I').pack
        (op, _) = algo.accept()
        with op:
            msg = assoc + plain
            op.sendmsg([msg], ([socket.SOL_ALG, socket.ALG_SET_OP, pack_uint32(socket.ALG_OP_ENCRYPT)], [socket.SOL_ALG, socket.ALG_SET_IV, pack_uint32(len(iv)) + iv], [socket.SOL_ALG, socket.ALG_SET_AEAD_ASSOCLEN, pack_uint32(assoclen)]))
            res = op.recv(len(msg) + taglen)
            self.assertEqual(expected_ct, res[assoclen:-taglen])
            self.assertEqual(expected_tag, res[-taglen:])
        (op, _) = algo.accept()
        with op:
            msg = assoc + expected_ct + expected_tag
            op.sendmsg_afalg([msg], op=socket.ALG_OP_DECRYPT, iv=iv, assoclen=assoclen)
            res = op.recv(len(msg) - taglen)
            self.assertEqual(plain, res[assoclen:])
