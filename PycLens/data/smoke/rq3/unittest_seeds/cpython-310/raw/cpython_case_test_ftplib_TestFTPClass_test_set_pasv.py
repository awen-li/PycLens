# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_set_pasv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.client.passiveserver)
    self.client.set_pasv(True)
    self.assertTrue(self.client.passiveserver)
    self.client.set_pasv(False)
    self.assertFalse(self.client.passiveserver)
