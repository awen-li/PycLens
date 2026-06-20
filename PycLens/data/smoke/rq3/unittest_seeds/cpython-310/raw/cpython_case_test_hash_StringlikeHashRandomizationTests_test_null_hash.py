# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: StringlikeHashRandomizationTests_test_null_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    known_hash_of_obj = self.get_expected_hash(0, 3)
    self.assertNotEqual(self.get_hash(self.repr_), known_hash_of_obj)
    self.assertEqual(self.get_hash(self.repr_, seed=0), known_hash_of_obj)
