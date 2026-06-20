# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: AppendTestBase_test_append_compressed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._create_testtar('w:' + self.suffix)
    self.assertRaises(tarfile.ReadError, tarfile.open, tmpname, 'a')
