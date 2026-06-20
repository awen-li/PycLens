# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_line_too_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ftplib.Error, self.client.sendcmd, 'x' * self.client.maxline * 2)
