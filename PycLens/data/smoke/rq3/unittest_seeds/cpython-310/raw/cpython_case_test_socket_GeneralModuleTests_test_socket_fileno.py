# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_socket_fileno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.addCleanup(s.close)
    s.bind((socket_helper.HOST, 0))
    self._test_socket_fileno(s, socket.AF_INET, socket.SOCK_STREAM)
    if hasattr(socket, 'SOCK_DGRAM'):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addCleanup(s.close)
        s.bind((socket_helper.HOST, 0))
        self._test_socket_fileno(s, socket.AF_INET, socket.SOCK_DGRAM)
    if socket_helper.IPV6_ENABLED:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.addCleanup(s.close)
        s.bind((socket_helper.HOSTv6, 0, 0, 0))
        self._test_socket_fileno(s, socket.AF_INET6, socket.SOCK_STREAM)
    if hasattr(socket, 'AF_UNIX'):
        tmpdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmpdir)
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.addCleanup(s.close)
        try:
            s.bind(os.path.join(tmpdir, 'socket'))
        except PermissionError:
            pass
        else:
            self._test_socket_fileno(s, socket.AF_UNIX, socket.SOCK_STREAM)
