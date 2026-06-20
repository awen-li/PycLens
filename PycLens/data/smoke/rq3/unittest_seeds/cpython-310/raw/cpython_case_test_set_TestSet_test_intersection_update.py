# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_intersection_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    retval = self.s.intersection_update(self.otherword)
    self.assertEqual(retval, None)
    for c in self.word + self.otherword:
        if c in self.otherword and c in self.word:
            self.assertIn(c, self.s)
        else:
            self.assertNotIn(c, self.s)
    self.assertRaises(PassThru, self.s.intersection_update, check_pass_thru())
    self.assertRaises(TypeError, self.s.intersection_update, [[]])
    for (p, q) in (('cdc', 'c'), ('efgfe', ''), ('ccb', 'bc'), ('ef', '')):
        for C in (set, frozenset, dict.fromkeys, str, list, tuple):
            s = self.thetype('abcba')
            self.assertEqual(s.intersection_update(C(p)), None)
            self.assertEqual(s, set(q))
            ss = 'abcba'
            s = self.thetype(ss)
            t = 'cbc'
            self.assertEqual(s.intersection_update(C(p), C(t)), None)
            self.assertEqual(s, set('abcba') & set(p) & set(t))
