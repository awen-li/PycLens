# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: StringlikeHashRandomizationTests_test_fixed_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = self.get_expected_hash(1, 3)
    self.assertEqual(self.get_hash(self.repr_, seed=42), h)
