# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommonReadTest_test_is_tarfile_erroneous

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(tmpname, 'wb'):
        pass
    self.assertFalse(tarfile.is_tarfile(tmpname))
    self.assertFalse(tarfile.is_tarfile(pathlib.Path(tmpname)))
    with open(tmpname, 'rb') as fobj:
        self.assertFalse(tarfile.is_tarfile(fobj))
    self.assertFalse(tarfile.is_tarfile(io.BytesIO(b'invalid')))
