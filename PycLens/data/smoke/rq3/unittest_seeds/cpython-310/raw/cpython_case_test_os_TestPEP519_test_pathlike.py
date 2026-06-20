# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestPEP519_test_pathlike

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('#feelthegil', self.fspath(FakePath('#feelthegil')))
    self.assertTrue(issubclass(FakePath, os.PathLike))
    self.assertTrue(isinstance(FakePath('x'), os.PathLike))
