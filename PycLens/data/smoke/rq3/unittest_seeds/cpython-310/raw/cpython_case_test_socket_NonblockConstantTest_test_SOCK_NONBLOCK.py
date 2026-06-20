# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: NonblockConstantTest_test_SOCK_NONBLOCK

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM | socket.SOCK_NONBLOCK) as s:
        self.checkNonblock(s)
        s.setblocking(True)
        self.checkNonblock(s, nonblock=False)
        s.setblocking(False)
        self.checkNonblock(s)
        s.settimeout(None)
        self.checkNonblock(s, nonblock=False)
        s.settimeout(2.0)
        self.checkNonblock(s, timeout=2.0)
        s.setblocking(True)
        self.checkNonblock(s, nonblock=False)
    t = socket.getdefaulttimeout()
    socket.setdefaulttimeout(0.0)
    with socket.socket() as s:
        self.checkNonblock(s)
    socket.setdefaulttimeout(None)
    with socket.socket() as s:
        self.checkNonblock(s, False)
    socket.setdefaulttimeout(2.0)
    with socket.socket() as s:
        self.checkNonblock(s, timeout=2.0)
    socket.setdefaulttimeout(None)
    with socket.socket() as s:
        self.checkNonblock(s, False)
    socket.setdefaulttimeout(t)
