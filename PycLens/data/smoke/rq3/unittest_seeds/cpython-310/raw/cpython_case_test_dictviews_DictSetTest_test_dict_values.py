# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_dict_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {1: 10, 'a': 'ABC'}
    values = d.values()
    self.assertEqual(set(values), {10, 'ABC'})
    self.assertEqual(len(values), 2)
