# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: TestFamilyDetection_test_socket_uses_IPv4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = smtpd.SMTPServer((socket_helper.HOSTv4, 0), (socket_helper.HOSTv6, 0))
    self.assertEqual(server.socket.family, socket.AF_INET)
