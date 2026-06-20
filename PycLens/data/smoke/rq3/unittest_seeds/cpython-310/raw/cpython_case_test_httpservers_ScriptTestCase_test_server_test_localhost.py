# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: ScriptTestCase_test_server_test_localhost

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mock_server = self.mock_server_class()
    server.test(ServerClass=mock_server, bind='localhost')
    self.assertIn(mock_server.address_family, (socket.AF_INET6, socket.AF_INET))
