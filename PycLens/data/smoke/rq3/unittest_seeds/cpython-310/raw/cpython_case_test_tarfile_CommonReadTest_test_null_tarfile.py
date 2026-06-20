# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommonReadTest_test_null_tarfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(tmpname, 'wb'):
        pass
    self.assertRaises(tarfile.ReadError, tarfile.open, tmpname, self.mode)
    self.assertRaises(tarfile.ReadError, tarfile.open, tmpname)
