# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestWithAscii_test_one_delete

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sm = difflib.SequenceMatcher(None, 'a' * 40 + 'c' + 'b' * 40, 'a' * 40 + 'b' * 40)
    self.assertAlmostEqual(sm.ratio(), 0.994, places=3)
    self.assertEqual(list(sm.get_opcodes()), [('equal', 0, 40, 0, 40), ('delete', 40, 41, 40, 40), ('equal', 41, 81, 40, 80)])
