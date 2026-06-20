# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: StringlikeHashRandomizationTests_test_long_fixed_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.repr_long is None:
        return
    h = self.get_expected_hash(2, 11)
    self.assertEqual(self.get_hash(self.repr_long, seed=42), h)
