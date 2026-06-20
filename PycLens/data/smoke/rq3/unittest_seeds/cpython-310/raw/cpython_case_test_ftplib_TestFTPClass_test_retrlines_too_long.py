# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_retrlines_too_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.sendcmd('SETLONGRETR %d' % (self.client.maxline * 2))
    received = []
    self.assertRaises(ftplib.Error, self.client.retrlines, 'retr', received.append)
