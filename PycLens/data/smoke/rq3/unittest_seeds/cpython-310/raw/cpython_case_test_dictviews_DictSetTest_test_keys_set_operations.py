# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_keys_set_operations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 2}
    d3 = {'d': 4, 'e': 5}
    d4 = {'d': 4}

    class CustomSet(set):

        def intersection(self, other):
            return CustomSet(super().intersection(other))
    self.assertEqual(d1.keys() & d1.keys(), {'a', 'b'})
    self.assertEqual(d1.keys() & d2.keys(), {'b'})
    self.assertEqual(d1.keys() & d3.keys(), set())
    self.assertEqual(d1.keys() & set(d1.keys()), {'a', 'b'})
    self.assertEqual(d1.keys() & set(d2.keys()), {'b'})
    self.assertEqual(d1.keys() & set(d3.keys()), set())
    self.assertEqual(d1.keys() & tuple(d1.keys()), {'a', 'b'})
    self.assertEqual(d3.keys() & d4.keys(), {'d'})
    self.assertEqual(d4.keys() & d3.keys(), {'d'})
    self.assertEqual(d4.keys() & set(d3.keys()), {'d'})
    self.assertIsInstance(d4.keys() & frozenset(d3.keys()), set)
    self.assertIsInstance(frozenset(d3.keys()) & d4.keys(), set)
    self.assertIs(type(d4.keys() & CustomSet(d3.keys())), set)
    self.assertIs(type(d1.keys() & []), set)
    self.assertIs(type([] & d1.keys()), set)
    self.assertEqual(d1.keys() | d1.keys(), {'a', 'b'})
    self.assertEqual(d1.keys() | d2.keys(), {'a', 'b', 'c'})
    self.assertEqual(d1.keys() | d3.keys(), {'a', 'b', 'd', 'e'})
    self.assertEqual(d1.keys() | set(d1.keys()), {'a', 'b'})
    self.assertEqual(d1.keys() | set(d2.keys()), {'a', 'b', 'c'})
    self.assertEqual(d1.keys() | set(d3.keys()), {'a', 'b', 'd', 'e'})
    self.assertEqual(d1.keys() | (1, 2), {'a', 'b', 1, 2})
    self.assertEqual(d1.keys() ^ d1.keys(), set())
    self.assertEqual(d1.keys() ^ d2.keys(), {'a', 'c'})
    self.assertEqual(d1.keys() ^ d3.keys(), {'a', 'b', 'd', 'e'})
    self.assertEqual(d1.keys() ^ set(d1.keys()), set())
    self.assertEqual(d1.keys() ^ set(d2.keys()), {'a', 'c'})
    self.assertEqual(d1.keys() ^ set(d3.keys()), {'a', 'b', 'd', 'e'})
    self.assertEqual(d1.keys() ^ tuple(d2.keys()), {'a', 'c'})
    self.assertEqual(d1.keys() - d1.keys(), set())
    self.assertEqual(d1.keys() - d2.keys(), {'a'})
    self.assertEqual(d1.keys() - d3.keys(), {'a', 'b'})
    self.assertEqual(d1.keys() - set(d1.keys()), set())
    self.assertEqual(d1.keys() - set(d2.keys()), {'a'})
    self.assertEqual(d1.keys() - set(d3.keys()), {'a', 'b'})
    self.assertEqual(d1.keys() - (0, 1), {'a', 'b'})
    self.assertFalse(d1.keys().isdisjoint(d1.keys()))
    self.assertFalse(d1.keys().isdisjoint(d2.keys()))
    self.assertFalse(d1.keys().isdisjoint(list(d2.keys())))
    self.assertFalse(d1.keys().isdisjoint(set(d2.keys())))
    self.assertTrue(d1.keys().isdisjoint({'x', 'y', 'z'}))
    self.assertTrue(d1.keys().isdisjoint(['x', 'y', 'z']))
    self.assertTrue(d1.keys().isdisjoint(set(['x', 'y', 'z'])))
    self.assertTrue(d1.keys().isdisjoint(set(['x', 'y'])))
    self.assertTrue(d1.keys().isdisjoint(['x', 'y']))
    self.assertTrue(d1.keys().isdisjoint({}))
    self.assertTrue(d1.keys().isdisjoint(d3.keys()))
    de = {}
    self.assertTrue(de.keys().isdisjoint(set()))
    self.assertTrue(de.keys().isdisjoint([]))
    self.assertTrue(de.keys().isdisjoint(de.keys()))
    self.assertTrue(de.keys().isdisjoint([1]))
