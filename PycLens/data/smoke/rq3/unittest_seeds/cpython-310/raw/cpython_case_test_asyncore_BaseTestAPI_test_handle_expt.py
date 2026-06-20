# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_handle_expt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if HAS_UNIX_SOCKETS and self.family == socket.AF_UNIX:
        self.skipTest('Not applicable to AF_UNIX sockets.')
    if sys.platform == 'darwin' and self.use_poll:
        self.skipTest('poll may fail on macOS; see issue #28087')

    class TestClient(BaseClient):

        def handle_expt(self):
            self.socket.recv(1024, socket.MSG_OOB)
            self.flag = True

    class TestHandler(BaseTestHandler):

        def __init__(self, conn):
            BaseTestHandler.__init__(self, conn)
            self.socket.send(bytes(chr(244), 'latin-1'), socket.MSG_OOB)
    server = BaseServer(self.family, self.addr, TestHandler)
    client = TestClient(self.family, server.address)
    self.loop_waiting_for_flag(client)
