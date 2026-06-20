# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_csocket_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    try:
        expected = '<socket object, fd=%s, family=%s, type=%s, proto=%s>' % (s.fileno(), s.family, s.type, s.proto)
        self.assertEqual(repr(s), expected)
    finally:
        s.close()
    expected = '<socket object, fd=-1, family=%s, type=%s, proto=%s>' % (s.family, s.type, s.proto)
    self.assertEqual(repr(s), expected)
