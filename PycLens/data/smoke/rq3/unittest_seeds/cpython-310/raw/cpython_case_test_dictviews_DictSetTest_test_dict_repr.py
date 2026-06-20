# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_dict_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {1: 10, 'a': 'ABC'}
    self.assertIsInstance(repr(d), str)
    r = repr(d.items())
    self.assertIsInstance(r, str)
    self.assertTrue(r == "dict_items([('a', 'ABC'), (1, 10)])" or r == "dict_items([(1, 10), ('a', 'ABC')])")
    r = repr(d.keys())
    self.assertIsInstance(r, str)
    self.assertTrue(r == "dict_keys(['a', 1])" or r == "dict_keys([1, 'a'])")
    r = repr(d.values())
    self.assertIsInstance(r, str)
    self.assertTrue(r == "dict_values(['ABC', 10])" or r == "dict_values([10, 'ABC'])")
