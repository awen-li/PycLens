# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: LinuxKernelCryptoAPI_test_drbg_pr_sha256

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.create_alg('rng', 'drbg_pr_sha256') as algo:
        extra_seed = os.urandom(32)
        algo.setsockopt(socket.SOL_ALG, socket.ALG_SET_KEY, extra_seed)
        (op, _) = algo.accept()
        with op:
            rn = op.recv(32)
            self.assertEqual(len(rn), 32)
