# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_combinations_with_replacement_tuple_reuse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cwr = combinations_with_replacement
    self.assertEqual(len(set(map(id, cwr('abcde', 3)))), 1)
    self.assertNotEqual(len(set(map(id, list(cwr('abcde', 3))))), 1)
