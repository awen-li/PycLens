# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_handle_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestClient(BaseClient):

        def handle_read(self):
            self.flag = True

    class TestHandler(BaseTestHandler):

        def __init__(self, conn):
            BaseTestHandler.__init__(self, conn)
            self.send(b'x' * 1024)
    server = BaseServer(self.family, self.addr, TestHandler)
    client = TestClient(self.family, server.address)
    self.loop_waiting_for_flag(client)
