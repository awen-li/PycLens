# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_non_blocking_connect_ex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = test_wrap_socket(socket.socket(socket.AF_INET), cert_reqs=ssl.CERT_REQUIRED, ca_certs=SIGNING_CA, do_handshake_on_connect=False)
    self.addCleanup(s.close)
    s.setblocking(False)
    rc = s.connect_ex(self.server_addr)
    self.assertIn(rc, (0, errno.EINPROGRESS, errno.EWOULDBLOCK))
    select.select([], [s], [], 5.0)
    while True:
        try:
            s.do_handshake()
            break
        except ssl.SSLWantReadError:
            select.select([s], [], [], 5.0)
        except ssl.SSLWantWriteError:
            select.select([], [s], [], 5.0)
    self.assertTrue(s.getpeercert())
