# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_name_closed_socketio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        fp = sock.makefile('rb')
        fp.close()
        self.assertEqual(repr(fp), '<_io.BufferedReader name=-1>')
