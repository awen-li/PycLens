# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: TestMSWindowsTCPFlags_test_new_tcp_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    provided = [s for s in dir(socket) if s.startswith('TCP')]
    unknown = [s for s in provided if s not in self.knownTCPFlags]
    self.assertEqual([], unknown, 'New TCP flags were discovered. See bpo-32394 for more information')
