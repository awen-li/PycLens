# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_symmetric_difference_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    retval = self.s.symmetric_difference_update(self.otherword)
    self.assertEqual(retval, None)
    for c in self.word + self.otherword:
        if (c in self.word) ^ (c in self.otherword):
            self.assertIn(c, self.s)
        else:
            self.assertNotIn(c, self.s)
    self.assertRaises(PassThru, self.s.symmetric_difference_update, check_pass_thru())
    self.assertRaises(TypeError, self.s.symmetric_difference_update, [[]])
    for (p, q) in (('cdc', 'abd'), ('efgfe', 'abcefg'), ('ccb', 'a'), ('ef', 'abcef')):
        for C in (set, frozenset, dict.fromkeys, str, list, tuple):
            s = self.thetype('abcba')
            self.assertEqual(s.symmetric_difference_update(C(p)), None)
            self.assertEqual(s, set(q))
