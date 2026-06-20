# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_valued_union_operators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = C()
    b = C()
    c = C()
    wvd1 = weakref.WeakValueDictionary({1: a})
    wvd2 = weakref.WeakValueDictionary({1: b, 2: a})
    wvd3 = wvd1.copy()
    d1 = {1: c, 3: b}
    pairs = [(5, c), (6, b)]
    tmp1 = wvd1 | wvd2
    self.assertEqual(dict(tmp1), dict(wvd1) | dict(wvd2))
    self.assertIs(type(tmp1), weakref.WeakValueDictionary)
    wvd1 |= wvd2
    self.assertEqual(wvd1, tmp1)
    tmp2 = wvd2 | d1
    self.assertEqual(dict(tmp2), dict(wvd2) | d1)
    self.assertIs(type(tmp2), weakref.WeakValueDictionary)
    wvd2 |= d1
    self.assertEqual(wvd2, tmp2)
    tmp3 = wvd3.copy()
    tmp3 |= pairs
    self.assertEqual(dict(tmp3), dict(wvd3) | dict(pairs))
    self.assertIs(type(tmp3), weakref.WeakValueDictionary)
    tmp4 = d1 | wvd3
    self.assertEqual(dict(tmp4), d1 | dict(wvd3))
    self.assertIs(type(tmp4), weakref.WeakValueDictionary)
    del a
    self.assertNotIn(2, tmp1)
    self.assertNotIn(2, tmp2)
    self.assertNotIn(1, tmp3)
    self.assertNotIn(1, tmp4)
