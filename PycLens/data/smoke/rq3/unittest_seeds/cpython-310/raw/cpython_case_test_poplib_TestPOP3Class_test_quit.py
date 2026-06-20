# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poplib.py
# case: TestPOP3Class_test_quit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    resp = self.client.quit()
    self.assertTrue(resp)
    self.assertIsNone(self.client.sock)
    self.assertIsNone(self.client.file)
