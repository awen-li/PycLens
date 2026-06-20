# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestMutate_test_update_unit_tuple_non_overlap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.set.update(('a', 'z'))
    self.assertEqual(self.set, set(self.values + ['z']))
