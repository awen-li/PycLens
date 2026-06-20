# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: SeqTestCase_test_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.o.ind = 1
    self.o2.ind = 3
    self.n.ind = 2
    self.n2.ind = 4
    self.assertEqual(self.seq[self.o:self.o2], self.seq[1:3])
    self.assertEqual(self.seq[self.n:self.n2], self.seq[2:4])
