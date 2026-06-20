# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket()
    with sock:
        for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
            self.assertRaises(TypeError, pickle.dumps, sock, protocol)
    for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
        family = pickle.loads(pickle.dumps(socket.AF_INET, protocol))
        self.assertEqual(family, socket.AF_INET)
        type = pickle.loads(pickle.dumps(socket.SOCK_STREAM, protocol))
        self.assertEqual(type, socket.SOCK_STREAM)
