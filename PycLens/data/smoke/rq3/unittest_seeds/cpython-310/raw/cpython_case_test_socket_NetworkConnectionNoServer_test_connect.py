# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: NetworkConnectionNoServer_test_connect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    port = socket_helper.find_unused_port()
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.addCleanup(cli.close)
    with self.assertRaises(OSError) as cm:
        cli.connect((HOST, port))
    self.assertEqual(cm.exception.errno, errno.ECONNREFUSED)
