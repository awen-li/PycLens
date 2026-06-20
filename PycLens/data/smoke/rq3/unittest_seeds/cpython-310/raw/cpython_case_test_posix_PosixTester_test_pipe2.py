# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_pipe2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, os.pipe2, 'DEADBEEF')
    self.assertRaises(TypeError, os.pipe2, 0, 0)
    (r, w) = os.pipe2(0)
    os.close(r)
    os.close(w)
    (r, w) = os.pipe2(os.O_CLOEXEC | os.O_NONBLOCK)
    self.addCleanup(os.close, r)
    self.addCleanup(os.close, w)
    self.assertFalse(os.get_inheritable(r))
    self.assertFalse(os.get_inheritable(w))
    self.assertFalse(os.get_blocking(r))
    self.assertFalse(os.get_blocking(w))
    self.assertRaises(OSError, os.read, r, 1)
    try:
        os.write(w, b'x' * support.PIPE_MAX_SIZE)
    except OSError:
        pass
