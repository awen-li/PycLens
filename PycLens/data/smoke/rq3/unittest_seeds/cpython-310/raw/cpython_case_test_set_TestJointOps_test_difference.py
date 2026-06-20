# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_difference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = self.s.difference(self.otherword)
    for c in self.letters:
        self.assertEqual(c in i, c in self.d and c not in self.otherword)
    self.assertEqual(self.s, self.thetype(self.word))
    self.assertEqual(type(i), self.basetype)
    self.assertRaises(PassThru, self.s.difference, check_pass_thru())
    self.assertRaises(TypeError, self.s.difference, [[]])
    for C in (set, frozenset, dict.fromkeys, str, list, tuple):
        self.assertEqual(self.thetype('abcba').difference(C('cdc')), set('ab'))
        self.assertEqual(self.thetype('abcba').difference(C('efgfe')), set('abc'))
        self.assertEqual(self.thetype('abcba').difference(C('ccb')), set('a'))
        self.assertEqual(self.thetype('abcba').difference(C('ef')), set('abc'))
        self.assertEqual(self.thetype('abcba').difference(), set('abc'))
        self.assertEqual(self.thetype('abcba').difference(C('a'), C('b')), set('c'))
