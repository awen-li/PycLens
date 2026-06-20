# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: NetworkConnectionNoServer_test_create_connection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    port = socket_helper.find_unused_port()
    with self.assertRaises(OSError) as cm:
        socket.create_connection((HOST, port))
    expected_errnos = socket_helper.get_socket_conn_refused_errs()
    self.assertIn(cm.exception.errno, expected_errnos)
