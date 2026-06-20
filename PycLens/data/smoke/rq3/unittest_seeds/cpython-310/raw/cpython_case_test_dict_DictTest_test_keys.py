# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    self.assertEqual(set(d.keys()), set())
    d = {'a': 1, 'b': 2}
    k = d.keys()
    self.assertEqual(set(k), {'a', 'b'})
    self.assertIn('a', k)
    self.assertIn('b', k)
    self.assertIn('a', d)
    self.assertIn('b', d)
    self.assertRaises(TypeError, d.keys, None)
    self.assertEqual(repr(dict(a=1).keys()), "dict_keys(['a'])")
