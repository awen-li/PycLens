# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestTLS_FTPClass_test_ccc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, self.client.ccc)
    self.client.login(secure=True)
    self.assertIsInstance(self.client.sock, ssl.SSLSocket)
    self.client.ccc()
    self.assertRaises(ValueError, self.client.sock.unwrap)
