# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_fail_comp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(tarfile.ReadError, tarfile.open, tarname, self.mode)
    with open(tarname, 'rb') as fobj:
        self.assertRaises(tarfile.ReadError, tarfile.open, fileobj=fobj, mode=self.mode)
