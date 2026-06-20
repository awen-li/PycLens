# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: CapsAfterLoginNNTPv2Tests_test_caps_only_after_login

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.server._caps, {})
    self.server.login('testuser', 'testpw')
    self.assertIn('VERSION', self.server._caps)
