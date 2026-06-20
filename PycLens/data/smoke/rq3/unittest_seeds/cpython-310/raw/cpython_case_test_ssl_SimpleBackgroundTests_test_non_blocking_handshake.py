# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_non_blocking_handshake

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.socket(socket.AF_INET)
    s.connect(self.server_addr)
    s.setblocking(False)
    s = test_wrap_socket(s, cert_reqs=ssl.CERT_NONE, do_handshake_on_connect=False)
    self.addCleanup(s.close)
    count = 0
    while True:
        try:
            count += 1
            s.do_handshake()
            break
        except ssl.SSLWantReadError:
            select.select([s], [], [])
        except ssl.SSLWantWriteError:
            select.select([], [s], [])
    if support.verbose:
        sys.stdout.write('\nNeeded %d calls to do_handshake() to establish session.\n' % count)
