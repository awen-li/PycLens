# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_ciphers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with test_wrap_socket(socket.socket(socket.AF_INET), cert_reqs=ssl.CERT_NONE, ciphers='ALL') as s:
        s.connect(self.server_addr)
    with test_wrap_socket(socket.socket(socket.AF_INET), cert_reqs=ssl.CERT_NONE, ciphers='DEFAULT') as s:
        s.connect(self.server_addr)
    with self.assertRaisesRegex(ssl.SSLError, 'No cipher can be selected'):
        with socket.socket(socket.AF_INET) as sock:
            s = test_wrap_socket(sock, cert_reqs=ssl.CERT_NONE, ciphers="^$:,;?*'dorothyx")
            s.connect(self.server_addr)
