# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_dict_items

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {1: 10, 'a': 'ABC'}
    items = d.items()
    self.assertEqual(len(items), 2)
    self.assertEqual(set(items), {(1, 10), ('a', 'ABC')})
    self.assertEqual(items, {(1, 10), ('a', 'ABC')})
    self.assertNotEqual(items, {(1, 10), ('a', 'ABC'), 'junk'})
    self.assertNotEqual(items, {(1, 10), ('a', 'def')})
    self.assertNotEqual(items, {(1, 10)})
    self.assertNotEqual(items, 42)
    self.assertIn((1, 10), items)
    self.assertIn(('a', 'ABC'), items)
    self.assertNotIn((1, 11), items)
    self.assertNotIn(1, items)
    self.assertNotIn((), items)
    self.assertNotIn((1,), items)
    self.assertNotIn((1, 2, 3), items)
    self.assertEqual(d.items(), d.items())
    e = d.copy()
    self.assertEqual(d.items(), e.items())
    e['a'] = 'def'
    self.assertNotEqual(d.items(), e.items())
