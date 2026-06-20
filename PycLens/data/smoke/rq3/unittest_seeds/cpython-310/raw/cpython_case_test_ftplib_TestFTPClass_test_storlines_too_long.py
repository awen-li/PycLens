# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_storlines_too_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.BytesIO(b'x' * self.client.maxline * 2)
    self.assertRaises(ftplib.Error, self.client.storlines, 'stor', f)
