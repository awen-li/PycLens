# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_create_socket

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = asyncore.dispatcher()
    s.create_socket(self.family)
    self.assertEqual(s.socket.type, socket.SOCK_STREAM)
    self.assertEqual(s.socket.family, self.family)
    self.assertEqual(s.socket.gettimeout(), 0)
    self.assertFalse(s.socket.get_inheritable())
