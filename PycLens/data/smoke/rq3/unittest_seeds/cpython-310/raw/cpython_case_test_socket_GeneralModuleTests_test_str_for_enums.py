# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_str_for_enums

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        self.assertEqual(str(s.family), 'AddressFamily.AF_INET')
        self.assertEqual(str(s.type), 'SocketKind.SOCK_STREAM')
