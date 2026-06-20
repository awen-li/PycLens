# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_parallel_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(self.tarname) as tar:
        for (m1, m2) in zip(tar, tar):
            self.assertEqual(m1.offset, m2.offset)
            self.assertEqual(m1.get_info(), m2.get_info())
