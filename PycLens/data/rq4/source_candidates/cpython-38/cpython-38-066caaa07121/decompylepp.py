# Source Generated with Decompyle++
# File: cpython-38-066caaa07121.pyc (Python 3.8)


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

for None in '__main__':
    if None:
        __pybcsec_seed__()
    return None
