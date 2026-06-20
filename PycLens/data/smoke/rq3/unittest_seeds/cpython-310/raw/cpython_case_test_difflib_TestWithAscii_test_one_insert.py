# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestWithAscii_test_one_insert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sm = difflib.SequenceMatcher(None, 'b' * 100, 'a' + 'b' * 100)
    self.assertAlmostEqual(sm.ratio(), 0.995, places=3)
    self.assertEqual(list(sm.get_opcodes()), [('insert', 0, 0, 0, 1), ('equal', 0, 100, 1, 101)])
    self.assertEqual(sm.bpopular, set())
    sm = difflib.SequenceMatcher(None, 'b' * 100, 'b' * 50 + 'a' + 'b' * 50)
    self.assertAlmostEqual(sm.ratio(), 0.995, places=3)
    self.assertEqual(list(sm.get_opcodes()), [('equal', 0, 50, 0, 50), ('insert', 50, 50, 50, 51), ('equal', 50, 100, 51, 101)])
    self.assertEqual(sm.bpopular, set())
