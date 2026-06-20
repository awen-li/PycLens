# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_sethostname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    oldhn = socket.gethostname()
    try:
        socket.sethostname('new')
    except OSError as e:
        if e.errno == errno.EPERM:
            self.skipTest('test should be run as root')
        else:
            raise
    try:
        self.assertEqual(socket.gethostname(), 'new')
        socket.sethostname(b'bar')
        self.assertEqual(socket.gethostname(), 'bar')
    finally:
        socket.sethostname(oldhn)
