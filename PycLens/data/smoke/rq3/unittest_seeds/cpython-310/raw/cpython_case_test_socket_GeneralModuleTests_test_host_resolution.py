# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_host_resolution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for addr in [socket_helper.HOSTv4, '10.0.0.1', '255.255.255.255']:
        self.assertEqual(socket.gethostbyname(addr), addr)
    for host in [socket_helper.HOSTv4]:
        self.assertIn(host, socket.gethostbyaddr(host)[2])
