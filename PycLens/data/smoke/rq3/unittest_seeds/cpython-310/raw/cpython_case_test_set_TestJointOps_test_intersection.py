# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_intersection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = self.s.intersection(self.otherword)
    for c in self.letters:
        self.assertEqual(c in i, c in self.d and c in self.otherword)
    self.assertEqual(self.s, self.thetype(self.word))
    self.assertEqual(type(i), self.basetype)
    self.assertRaises(PassThru, self.s.intersection, check_pass_thru())
    for C in (set, frozenset, dict.fromkeys, str, list, tuple):
        self.assertEqual(self.thetype('abcba').intersection(C('cdc')), set('cc'))
        self.assertEqual(self.thetype('abcba').intersection(C('efgfe')), set(''))
        self.assertEqual(self.thetype('abcba').intersection(C('ccb')), set('bc'))
        self.assertEqual(self.thetype('abcba').intersection(C('ef')), set(''))
        self.assertEqual(self.thetype('abcba').intersection(C('cbcf'), C('bag')), set('b'))
    s = self.thetype('abcba')
    z = s.intersection()
    if self.thetype == frozenset():
        self.assertEqual(id(s), id(z))
    else:
        self.assertNotEqual(id(s), id(z))
