# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_keyed_union_operators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o1 = C()
    o2 = C()
    o3 = C()
    wkd1 = weakref.WeakKeyDictionary({o1: 1, o2: 2})
    wkd2 = weakref.WeakKeyDictionary({o3: 3, o1: 4})
    wkd3 = wkd1.copy()
    d1 = {o2: '5', o3: '6'}
    pairs = [(o2, 7), (o3, 8)]
    tmp1 = wkd1 | wkd2
    self.assertEqual(dict(tmp1), dict(wkd1) | dict(wkd2))
    self.assertIs(type(tmp1), weakref.WeakKeyDictionary)
    wkd1 |= wkd2
    self.assertEqual(wkd1, tmp1)
    tmp2 = wkd2 | d1
    self.assertEqual(dict(tmp2), dict(wkd2) | d1)
    self.assertIs(type(tmp2), weakref.WeakKeyDictionary)
    wkd2 |= d1
    self.assertEqual(wkd2, tmp2)
    tmp3 = wkd3.copy()
    tmp3 |= pairs
    self.assertEqual(dict(tmp3), dict(wkd3) | dict(pairs))
    self.assertIs(type(tmp3), weakref.WeakKeyDictionary)
    tmp4 = d1 | wkd3
    self.assertEqual(dict(tmp4), d1 | dict(wkd3))
    self.assertIs(type(tmp4), weakref.WeakKeyDictionary)
    del o1
    self.assertNotIn(4, tmp1.values())
    self.assertNotIn(4, tmp2.values())
    self.assertNotIn(1, tmp3.values())
    self.assertNotIn(1, tmp4.values())
