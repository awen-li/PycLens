# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: RemoteIMAP_STARTTLSTest_test_logincapa

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for cap in self.server.capabilities:
        self.assertIsInstance(cap, str)
    self.assertNotIn('LOGINDISABLED', self.server.capabilities)
