# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_unusable_closed_socketio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.socket() as sock:
        fp = sock.makefile('rb', buffering=0)
        self.assertTrue(fp.readable())
        self.assertFalse(fp.writable())
        self.assertFalse(fp.seekable())
        fp.close()
        self.assertRaises(ValueError, fp.readable)
        self.assertRaises(ValueError, fp.writable)
        self.assertRaises(ValueError, fp.seekable)
