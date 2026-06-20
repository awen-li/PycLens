# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_handle_accepted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestListener(BaseTestHandler):

        def __init__(self, family, addr):
            BaseTestHandler.__init__(self)
            self.create_socket(family)
            bind_af_aware(self.socket, addr)
            self.listen(5)
            self.address = self.socket.getsockname()

        def handle_accept(self):
            asyncore.dispatcher.handle_accept(self)

        def handle_accepted(self, sock, addr):
            sock.close()
            self.flag = True
    server = TestListener(self.family, self.addr)
    client = BaseClient(self.family, server.address)
    self.loop_waiting_for_flag(server)
