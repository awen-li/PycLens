# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_dict_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {1: 10, 'a': 'ABC'}
    keys = d.keys()
    self.assertEqual(len(keys), 2)
    self.assertEqual(set(keys), {1, 'a'})
    self.assertEqual(keys, {1, 'a'})
    self.assertNotEqual(keys, {1, 'a', 'b'})
    self.assertNotEqual(keys, {1, 'b'})
    self.assertNotEqual(keys, {1})
    self.assertNotEqual(keys, 42)
    self.assertIn(1, keys)
    self.assertIn('a', keys)
    self.assertNotIn(10, keys)
    self.assertNotIn('Z', keys)
    self.assertEqual(d.keys(), d.keys())
    e = {1: 11, 'a': 'def'}
    self.assertEqual(d.keys(), e.keys())
    del e['a']
    self.assertNotEqual(d.keys(), e.keys())
