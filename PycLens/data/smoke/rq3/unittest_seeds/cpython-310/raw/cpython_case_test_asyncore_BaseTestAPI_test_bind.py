# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_bind

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if HAS_UNIX_SOCKETS and self.family == socket.AF_UNIX:
        self.skipTest('Not applicable to AF_UNIX sockets.')
    s1 = asyncore.dispatcher()
    s1.create_socket(self.family)
    s1.bind(self.addr)
    s1.listen(5)
    port = s1.socket.getsockname()[1]
    s2 = asyncore.dispatcher()
    s2.create_socket(self.family)
    self.assertRaises(OSError, s2.bind, (self.addr[0], port))
