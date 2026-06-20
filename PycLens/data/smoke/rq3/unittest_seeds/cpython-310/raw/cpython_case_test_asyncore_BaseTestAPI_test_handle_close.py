# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_handle_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestClient(BaseClient):

        def handle_read(self):
            self.recv(1024)

        def handle_close(self):
            self.flag = True
            self.close()

    class TestHandler(BaseTestHandler):

        def __init__(self, conn):
            BaseTestHandler.__init__(self, conn)
            self.close()
    server = BaseServer(self.family, self.addr, TestHandler)
    client = TestClient(self.family, server.address)
    self.loop_waiting_for_flag(client)
