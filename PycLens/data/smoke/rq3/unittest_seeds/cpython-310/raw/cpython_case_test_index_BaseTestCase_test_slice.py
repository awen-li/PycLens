# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: BaseTestCase_test_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.o.ind = 1
    self.n.ind = 2
    slc = slice(self.o, self.o, self.o)
    check_slc = slice(1, 1, 1)
    self.assertEqual(slc.indices(self.o), check_slc.indices(1))
    slc = slice(self.n, self.n, self.n)
    check_slc = slice(2, 2, 2)
    self.assertEqual(slc.indices(self.n), check_slc.indices(2))
