# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_Sequence_mixins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SequenceSubclass(Sequence):

        def __init__(self, seq=()):
            self.seq = seq

        def __getitem__(self, index):
            return self.seq[index]

        def __len__(self):
            return len(self.seq)

    def assert_index_same(seq1, seq2, index_args):
        try:
            expected = seq1.index(*index_args)
        except ValueError:
            with self.assertRaises(ValueError):
                seq2.index(*index_args)
        else:
            actual = seq2.index(*index_args)
            self.assertEqual(actual, expected, '%r.index%s' % (seq1, index_args))
    for ty in (list, str):
        nativeseq = ty('abracadabra')
        indexes = [-10000, -9999] + list(range(-3, len(nativeseq) + 3))
        seqseq = SequenceSubclass(nativeseq)
        for letter in set(nativeseq) | {'z'}:
            assert_index_same(nativeseq, seqseq, (letter,))
            for start in range(-3, len(nativeseq) + 3):
                assert_index_same(nativeseq, seqseq, (letter, start))
                for stop in range(-3, len(nativeseq) + 3):
                    assert_index_same(nativeseq, seqseq, (letter, start, stop))
