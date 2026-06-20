# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: NetworkedTests_test_timeout_connect_ex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket_helper.transient_internet(REMOTE_HOST):
        s = test_wrap_socket(socket.socket(socket.AF_INET), cert_reqs=ssl.CERT_REQUIRED, do_handshake_on_connect=False)
        self.addCleanup(s.close)
        s.settimeout(1e-07)
        rc = s.connect_ex((REMOTE_HOST, 443))
        if rc == 0:
            self.skipTest('REMOTE_HOST responded too quickly')
        elif rc == errno.ENETUNREACH:
            self.skipTest('Network unreachable.')
        self.assertIn(rc, (errno.EAGAIN, errno.EWOULDBLOCK))
