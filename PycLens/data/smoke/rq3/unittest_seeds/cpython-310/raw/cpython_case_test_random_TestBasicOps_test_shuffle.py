# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_shuffle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    shuffle = self.gen.shuffle
    lst = []
    shuffle(lst)
    self.assertEqual(lst, [])
    lst = [37]
    shuffle(lst)
    self.assertEqual(lst, [37])
    seqs = [list(range(n)) for n in range(10)]
    shuffled_seqs = [list(range(n)) for n in range(10)]
    for shuffled_seq in shuffled_seqs:
        shuffle(shuffled_seq)
    for (seq, shuffled_seq) in zip(seqs, shuffled_seqs):
        self.assertEqual(len(seq), len(shuffled_seq))
        self.assertEqual(set(seq), set(shuffled_seq))
    lst = list(range(1000))
    shuffled_lst = list(range(1000))
    shuffle(shuffled_lst)
    self.assertTrue(lst != shuffled_lst)
    shuffle(lst)
    self.assertTrue(lst != shuffled_lst)
    self.assertRaises(TypeError, shuffle, (1, 2, 3))
