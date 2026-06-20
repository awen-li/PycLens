# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: RemoteIMAP_SSLTest_test_logout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket_helper.transient_internet(self.host):
        _server = self.imap_class(self.host, self.port)
        rs = _server.logout()
        self.assertEqual(rs[0], 'BYE', rs)
