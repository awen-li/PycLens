# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_authinfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.nntp_version == 2:
        self.assertIn('AUTHINFO', self.server._caps)
    self.server.login('testuser', 'testpw')
    self.assertNotIn('AUTHINFO', self.server._caps)
