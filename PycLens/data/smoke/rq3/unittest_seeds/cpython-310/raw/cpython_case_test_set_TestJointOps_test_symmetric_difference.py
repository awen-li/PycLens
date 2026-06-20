# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_symmetric_difference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = self.s.symmetric_difference(self.otherword)
    for c in self.letters:
        self.assertEqual(c in i, (c in self.d) ^ (c in self.otherword))
    self.assertEqual(self.s, self.thetype(self.word))
    self.assertEqual(type(i), self.basetype)
    self.assertRaises(PassThru, self.s.symmetric_difference, check_pass_thru())
    self.assertRaises(TypeError, self.s.symmetric_difference, [[]])
    for C in (set, frozenset, dict.fromkeys, str, list, tuple):
        self.assertEqual(self.thetype('abcba').symmetric_difference(C('cdc')), set('abd'))
        self.assertEqual(self.thetype('abcba').symmetric_difference(C('efgfe')), set('abcefg'))
        self.assertEqual(self.thetype('abcba').symmetric_difference(C('ccb')), set('a'))
        self.assertEqual(self.thetype('abcba').symmetric_difference(C('ef')), set('abcef'))
