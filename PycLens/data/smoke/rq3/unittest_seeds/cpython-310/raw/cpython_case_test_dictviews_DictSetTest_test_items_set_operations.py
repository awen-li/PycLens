# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_items_set_operations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 2, 'b': 2}
    d3 = {'d': 4, 'e': 5}
    self.assertEqual(d1.items() & d1.items(), {('a', 1), ('b', 2)})
    self.assertEqual(d1.items() & d2.items(), {('b', 2)})
    self.assertEqual(d1.items() & d3.items(), set())
    self.assertEqual(d1.items() & set(d1.items()), {('a', 1), ('b', 2)})
    self.assertEqual(d1.items() & set(d2.items()), {('b', 2)})
    self.assertEqual(d1.items() & set(d3.items()), set())
    self.assertEqual(d1.items() | d1.items(), {('a', 1), ('b', 2)})
    self.assertEqual(d1.items() | d2.items(), {('a', 1), ('a', 2), ('b', 2)})
    self.assertEqual(d1.items() | d3.items(), {('a', 1), ('b', 2), ('d', 4), ('e', 5)})
    self.assertEqual(d1.items() | set(d1.items()), {('a', 1), ('b', 2)})
    self.assertEqual(d1.items() | set(d2.items()), {('a', 1), ('a', 2), ('b', 2)})
    self.assertEqual(d1.items() | set(d3.items()), {('a', 1), ('b', 2), ('d', 4), ('e', 5)})
    self.assertEqual(d1.items() ^ d1.items(), set())
    self.assertEqual(d1.items() ^ d2.items(), {('a', 1), ('a', 2)})
    self.assertEqual(d1.items() ^ d3.items(), {('a', 1), ('b', 2), ('d', 4), ('e', 5)})
    self.assertEqual(d1.items() - d1.items(), set())
    self.assertEqual(d1.items() - d2.items(), {('a', 1)})
    self.assertEqual(d1.items() - d3.items(), {('a', 1), ('b', 2)})
    self.assertEqual(d1.items() - set(d1.items()), set())
    self.assertEqual(d1.items() - set(d2.items()), {('a', 1)})
    self.assertEqual(d1.items() - set(d3.items()), {('a', 1), ('b', 2)})
    self.assertFalse(d1.items().isdisjoint(d1.items()))
    self.assertFalse(d1.items().isdisjoint(d2.items()))
    self.assertFalse(d1.items().isdisjoint(list(d2.items())))
    self.assertFalse(d1.items().isdisjoint(set(d2.items())))
    self.assertTrue(d1.items().isdisjoint({'x', 'y', 'z'}))
    self.assertTrue(d1.items().isdisjoint(['x', 'y', 'z']))
    self.assertTrue(d1.items().isdisjoint(set(['x', 'y', 'z'])))
    self.assertTrue(d1.items().isdisjoint(set(['x', 'y'])))
    self.assertTrue(d1.items().isdisjoint({}))
    self.assertTrue(d1.items().isdisjoint(d3.items()))
    de = {}
    self.assertTrue(de.items().isdisjoint(set()))
    self.assertTrue(de.items().isdisjoint([]))
    self.assertTrue(de.items().isdisjoint(de.items()))
    self.assertTrue(de.items().isdisjoint([1]))
