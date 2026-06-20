# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    retval = self.s.update(self.otherword)
    self.assertEqual(retval, None)
    for c in self.word + self.otherword:
        self.assertIn(c, self.s)
    self.assertRaises(PassThru, self.s.update, check_pass_thru())
    self.assertRaises(TypeError, self.s.update, [[]])
    for (p, q) in (('cdc', 'abcd'), ('efgfe', 'abcefg'), ('ccb', 'abc'), ('ef', 'abcef')):
        for C in (set, frozenset, dict.fromkeys, str, list, tuple):
            s = self.thetype('abcba')
            self.assertEqual(s.update(C(p)), None)
            self.assertEqual(s, set(q))
    for p in ('cdc', 'efgfe', 'ccb', 'ef', 'abcda'):
        q = 'ahi'
        for C in (set, frozenset, dict.fromkeys, str, list, tuple):
            s = self.thetype('abcba')
            self.assertEqual(s.update(C(p), C(q)), None)
            self.assertEqual(s, set(s) | set(p) | set(q))
