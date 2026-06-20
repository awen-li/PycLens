# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_quick_connect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.family not in (socket.AF_INET, getattr(socket, 'AF_INET6', object())):
        self.skipTest('test specific to AF_INET and AF_INET6')
    server = BaseServer(self.family, self.addr)
    t = threading.Thread(target=lambda : asyncore.loop(timeout=0.1, count=5))
    t.start()
    try:
        with socket.socket(self.family, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
            try:
                s.connect(server.address)
            except OSError:
                pass
    finally:
        threading_helper.join_thread(t)
