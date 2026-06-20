# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: SeqTestCase_test_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.o.ind = -2
    self.n.ind = 2
    self.assertEqual(self.seq[self.n], self.seq[2])
    self.assertEqual(self.seq[self.o], self.seq[-2])
