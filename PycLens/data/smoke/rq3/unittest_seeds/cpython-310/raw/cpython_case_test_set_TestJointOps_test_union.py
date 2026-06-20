# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_union

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = self.s.union(self.otherword)
    for c in self.letters:
        self.assertEqual(c in u, c in self.d or c in self.otherword)
    self.assertEqual(self.s, self.thetype(self.word))
    self.assertEqual(type(u), self.basetype)
    self.assertRaises(PassThru, self.s.union, check_pass_thru())
    self.assertRaises(TypeError, self.s.union, [[]])
    for C in (set, frozenset, dict.fromkeys, str, list, tuple):
        self.assertEqual(self.thetype('abcba').union(C('cdc')), set('abcd'))
        self.assertEqual(self.thetype('abcba').union(C('efgfe')), set('abcefg'))
        self.assertEqual(self.thetype('abcba').union(C('ccb')), set('abc'))
        self.assertEqual(self.thetype('abcba').union(C('ef')), set('abcef'))
        self.assertEqual(self.thetype('abcba').union(C('ef'), C('fg')), set('abcefg'))
    x = self.thetype()
    self.assertEqual(x.union(set([1]), x, set([2])), self.thetype([1, 2]))
