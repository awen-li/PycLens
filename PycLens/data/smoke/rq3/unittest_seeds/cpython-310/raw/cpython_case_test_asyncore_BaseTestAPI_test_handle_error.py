# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_handle_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestClient(BaseClient):

        def handle_write(self):
            1.0 / 0

        def handle_error(self):
            self.flag = True
            try:
                raise
            except ZeroDivisionError:
                pass
            else:
                raise Exception('exception not raised')
    server = BaseServer(self.family, self.addr)
    client = TestClient(self.family, server.address)
    self.loop_waiting_for_flag(client)
