# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestAutojunk_test_one_insert_homogenous_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    seq1 = 'b' * 200
    seq2 = 'a' + 'b' * 200
    sm = difflib.SequenceMatcher(None, seq1, seq2)
    self.assertAlmostEqual(sm.ratio(), 0, places=3)
    self.assertEqual(sm.bpopular, {'b'})
    sm = difflib.SequenceMatcher(None, seq1, seq2, autojunk=False)
    self.assertAlmostEqual(sm.ratio(), 0.9975, places=3)
    self.assertEqual(sm.bpopular, set())
