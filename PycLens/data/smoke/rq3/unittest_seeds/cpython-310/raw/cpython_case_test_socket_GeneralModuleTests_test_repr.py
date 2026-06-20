# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with s:
        self.assertIn('fd=%i' % s.fileno(), repr(s))
        self.assertIn('family=%s' % socket.AF_INET, repr(s))
        self.assertIn('type=%s' % socket.SOCK_STREAM, repr(s))
        self.assertIn('proto=0', repr(s))
        self.assertNotIn('raddr', repr(s))
        s.bind(('127.0.0.1', 0))
        self.assertIn('laddr', repr(s))
        self.assertIn(str(s.getsockname()), repr(s))
    self.assertIn('[closed]', repr(s))
    self.assertNotIn('laddr', repr(s))
