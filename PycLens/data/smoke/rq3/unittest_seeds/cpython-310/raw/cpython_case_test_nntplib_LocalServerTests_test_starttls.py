# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: LocalServerTests_test_starttls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    file = self.nntp.file
    sock = self.nntp.sock
    self.nntp.starttls()
    self.assertNotEqual(file, self.nntp.file)
    self.assertNotEqual(sock, self.nntp.sock)
    self.assertIsInstance(self.nntp.sock, ssl.SSLSocket)
    self.assertRaises(ValueError, self.nntp.starttls)
