# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: SeqTestCase_test_slice_bug7532

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    seqlen = len(self.seq)
    self.o.ind = int(seqlen * 1.5)
    self.n.ind = seqlen + 2
    self.assertEqual(self.seq[self.o:], self.seq[0:0])
    self.assertEqual(self.seq[:self.o], self.seq)
    self.assertEqual(self.seq[self.n:], self.seq[0:0])
    self.assertEqual(self.seq[:self.n], self.seq)
    self.o2.ind = -seqlen - 2
    self.n2.ind = -int(seqlen * 1.5)
    self.assertEqual(self.seq[self.o2:], self.seq)
    self.assertEqual(self.seq[:self.o2], self.seq[0:0])
    self.assertEqual(self.seq[self.n2:], self.seq)
    self.assertEqual(self.seq[:self.n2], self.seq[0:0])
