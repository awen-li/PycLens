# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_dealloc_warn

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r = repr(sock)
    with self.assertWarns(ResourceWarning) as cm:
        sock = None
        support.gc_collect()
    self.assertIn(r, str(cm.warning.args[0]))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    f = sock.makefile('rb')
    r = repr(sock)
    sock = None
    support.gc_collect()
    with self.assertWarns(ResourceWarning):
        f = None
        support.gc_collect()
