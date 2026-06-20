# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestTLS_FTPClass_test_data_connection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.client.transfercmd('list') as sock:
        self.assertNotIsInstance(sock, ssl.SSLSocket)
        self.assertEqual(sock.recv(1024), LIST_DATA.encode(self.client.encoding))
    self.assertEqual(self.client.voidresp(), '226 transfer complete')
    self.client.prot_p()
    with self.client.transfercmd('list') as sock:
        self.assertIsInstance(sock, ssl.SSLSocket)
        self.assertEqual(sock.recv(1024), LIST_DATA.encode(self.client.encoding))
    self.assertEqual(self.client.voidresp(), '226 transfer complete')
    self.client.prot_c()
    with self.client.transfercmd('list') as sock:
        self.assertNotIsInstance(sock, ssl.SSLSocket)
        self.assertEqual(sock.recv(1024), LIST_DATA.encode(self.client.encoding))
    self.assertEqual(self.client.voidresp(), '226 transfer complete')
