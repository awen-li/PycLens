# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_connection_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = BaseServer(self.family, self.addr)
    client = BaseClient(self.family, server.address)
    self.assertFalse(server.connected)
    self.assertTrue(server.accepting)
    self.assertFalse(client.accepting)
    asyncore.loop(timeout=0.01, use_poll=self.use_poll, count=100)
    self.assertFalse(server.connected)
    self.assertTrue(server.accepting)
    self.assertTrue(client.connected)
    self.assertFalse(client.accepting)
    client.close()
    self.assertFalse(server.connected)
    self.assertTrue(server.accepting)
    self.assertFalse(client.connected)
    self.assertFalse(client.accepting)
    server.close()
    self.assertFalse(server.connected)
    self.assertFalse(server.accepting)
