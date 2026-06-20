# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_dict_mixed_keys_items

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {(1, 1): 11, (2, 2): 22}
    e = {1: 1, 2: 2}
    self.assertEqual(d.keys(), e.items())
    self.assertNotEqual(d.items(), e.keys())
