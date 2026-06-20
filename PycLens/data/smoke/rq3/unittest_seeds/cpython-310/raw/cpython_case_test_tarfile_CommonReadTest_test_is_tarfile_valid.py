# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommonReadTest_test_is_tarfile_valid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(tarfile.is_tarfile(self.tarname))
    self.assertTrue(tarfile.is_tarfile(pathlib.Path(self.tarname)))
    with open(self.tarname, 'rb') as fobj:
        self.assertTrue(tarfile.is_tarfile(fobj))
    with open(self.tarname, 'rb') as fobj:
        self.assertTrue(tarfile.is_tarfile(io.BytesIO(fobj.read())))
