# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: SeqTestCase_test_wrappers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.o.ind = 4
    self.n.ind = 5
    self.assertEqual(self.seq.__getitem__(self.o), self.seq[4])
    self.assertEqual(self.seq.__mul__(self.o), self.seq * 4)
    self.assertEqual(self.seq.__rmul__(self.o), self.seq * 4)
    self.assertEqual(self.seq.__getitem__(self.n), self.seq[5])
    self.assertEqual(self.seq.__mul__(self.n), self.seq * 5)
    self.assertEqual(self.seq.__rmul__(self.n), self.seq * 5)
