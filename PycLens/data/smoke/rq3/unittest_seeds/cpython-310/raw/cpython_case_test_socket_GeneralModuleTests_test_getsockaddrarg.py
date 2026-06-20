# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_getsockaddrarg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket()
    self.addCleanup(sock.close)
    port = socket_helper.find_unused_port()
    big_port = port + 65536
    neg_port = port - 65536
    self.assertRaises(OverflowError, sock.bind, (HOST, big_port))
    self.assertRaises(OverflowError, sock.bind, (HOST, neg_port))
    for i in itertools.count():
        port = socket_helper.find_unused_port()
        try:
            sock.bind((HOST, port))
        except OSError as e:
            if e.errno != errno.EADDRINUSE or i == 5:
                raise
        else:
            break
