# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_Set_interoperability_with_real_sets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ListSet(Set):

        def __init__(self, elements=()):
            self.data = []
            for elem in elements:
                if elem not in self.data:
                    self.data.append(elem)

        def __contains__(self, elem):
            return elem in self.data

        def __iter__(self):
            return iter(self.data)

        def __len__(self):
            return len(self.data)

        def __repr__(self):
            return 'Set({!r})'.format(self.data)
    r1 = set('abc')
    r2 = set('bcd')
    r3 = set('abcde')
    f1 = ListSet('abc')
    f2 = ListSet('bcd')
    f3 = ListSet('abcde')
    l1 = list('abccba')
    l2 = list('bcddcb')
    l3 = list('abcdeedcba')
    target = r1 & r2
    self.assertSameSet(f1 & f2, target)
    self.assertSameSet(f1 & r2, target)
    self.assertSameSet(r2 & f1, target)
    self.assertSameSet(f1 & l2, target)
    target = r1 | r2
    self.assertSameSet(f1 | f2, target)
    self.assertSameSet(f1 | r2, target)
    self.assertSameSet(r2 | f1, target)
    self.assertSameSet(f1 | l2, target)
    fwd_target = r1 - r2
    rev_target = r2 - r1
    self.assertSameSet(f1 - f2, fwd_target)
    self.assertSameSet(f2 - f1, rev_target)
    self.assertSameSet(f1 - r2, fwd_target)
    self.assertSameSet(f2 - r1, rev_target)
    self.assertSameSet(r1 - f2, fwd_target)
    self.assertSameSet(r2 - f1, rev_target)
    self.assertSameSet(f1 - l2, fwd_target)
    self.assertSameSet(f2 - l1, rev_target)
    target = r1 ^ r2
    self.assertSameSet(f1 ^ f2, target)
    self.assertSameSet(f1 ^ r2, target)
    self.assertSameSet(r2 ^ f1, target)
    self.assertSameSet(f1 ^ l2, target)
    self.assertTrue(f1 < f3)
    self.assertFalse(f1 < f1)
    self.assertFalse(f1 < f2)
    self.assertTrue(r1 < f3)
    self.assertFalse(r1 < f1)
    self.assertFalse(r1 < f2)
    self.assertTrue(r1 < r3)
    self.assertFalse(r1 < r1)
    self.assertFalse(r1 < r2)
    with self.assertRaises(TypeError):
        f1 < l3
    with self.assertRaises(TypeError):
        f1 < l1
    with self.assertRaises(TypeError):
        f1 < l2
    self.assertTrue(f1 <= f3)
    self.assertTrue(f1 <= f1)
    self.assertFalse(f1 <= f2)
    self.assertTrue(r1 <= f3)
    self.assertTrue(r1 <= f1)
    self.assertFalse(r1 <= f2)
    self.assertTrue(r1 <= r3)
    self.assertTrue(r1 <= r1)
    self.assertFalse(r1 <= r2)
    with self.assertRaises(TypeError):
        f1 <= l3
    with self.assertRaises(TypeError):
        f1 <= l1
    with self.assertRaises(TypeError):
        f1 <= l2
    self.assertTrue(f3 > f1)
    self.assertFalse(f1 > f1)
    self.assertFalse(f2 > f1)
    self.assertTrue(r3 > r1)
    self.assertFalse(f1 > r1)
    self.assertFalse(f2 > r1)
    self.assertTrue(r3 > r1)
    self.assertFalse(r1 > r1)
    self.assertFalse(r2 > r1)
    with self.assertRaises(TypeError):
        f1 > l3
    with self.assertRaises(TypeError):
        f1 > l1
    with self.assertRaises(TypeError):
        f1 > l2
    self.assertTrue(f3 >= f1)
    self.assertTrue(f1 >= f1)
    self.assertFalse(f2 >= f1)
    self.assertTrue(r3 >= r1)
    self.assertTrue(f1 >= r1)
    self.assertFalse(f2 >= r1)
    self.assertTrue(r3 >= r1)
    self.assertTrue(r1 >= r1)
    self.assertFalse(r2 >= r1)
    with self.assertRaises(TypeError):
        f1 >= l3
    with self.assertRaises(TypeError):
        f1 >= l1
    with self.assertRaises(TypeError):
        f1 >= l2
    self.assertTrue(f1 == f1)
    self.assertTrue(r1 == f1)
    self.assertTrue(f1 == r1)
    self.assertFalse(f1 == f3)
    self.assertFalse(r1 == f3)
    self.assertFalse(f1 == r3)
    self.assertFalse(f1 == l3)
    self.assertFalse(f1 == l1)
    self.assertFalse(f1 == l2)
    self.assertFalse(f1 != f1)
    self.assertFalse(r1 != f1)
    self.assertFalse(f1 != r1)
    self.assertTrue(f1 != f3)
    self.assertTrue(r1 != f3)
    self.assertTrue(f1 != r3)
    self.assertTrue(f1 != l3)
    self.assertTrue(f1 != l1)
    self.assertTrue(f1 != l2)
