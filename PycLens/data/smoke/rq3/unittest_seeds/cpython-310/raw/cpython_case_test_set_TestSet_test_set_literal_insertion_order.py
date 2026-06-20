# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_set_literal_insertion_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = {1, 1.0, True}
    self.assertEqual(len(s), 1)
    stored_value = s.pop()
    self.assertEqual(type(stored_value), int)
