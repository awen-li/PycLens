# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: LinuxKernelCryptoAPI_test_sendmsg_afalg_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket(socket.AF_ALG, socket.SOCK_SEQPACKET, 0)
    with sock:
        with self.assertRaises(TypeError):
            sock.sendmsg_afalg()
        with self.assertRaises(TypeError):
            sock.sendmsg_afalg(op=None)
        with self.assertRaises(TypeError):
            sock.sendmsg_afalg(1)
        with self.assertRaises(TypeError):
            sock.sendmsg_afalg(op=socket.ALG_OP_ENCRYPT, assoclen=None)
        with self.assertRaises(TypeError):
            sock.sendmsg_afalg(op=socket.ALG_OP_ENCRYPT, assoclen=-1)
