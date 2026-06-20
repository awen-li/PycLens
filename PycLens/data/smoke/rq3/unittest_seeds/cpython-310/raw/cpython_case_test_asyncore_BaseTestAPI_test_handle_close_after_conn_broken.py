# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_handle_close_after_conn_broken

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'\x00' * 128

    class TestClient(BaseClient):

        def handle_write(self):
            self.send(data)

        def handle_close(self):
            self.flag = True
            self.close()

        def handle_expt(self):
            self.flag = True
            self.close()

    class TestHandler(BaseTestHandler):

        def handle_read(self):
            self.recv(len(data))
            self.close()

        def writable(self):
            return False
    server = BaseServer(self.family, self.addr, TestHandler)
    client = TestClient(self.family, server.address)
    self.loop_waiting_for_flag(client)
