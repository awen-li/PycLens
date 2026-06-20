# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: StrHashRandomizationTests_test_ucs2_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = self.get_expected_hash(3, 6)
    self.assertEqual(self.get_hash(self.repr_ucs2, seed=0), h)
    h = self.get_expected_hash(4, 6)
    self.assertEqual(self.get_hash(self.repr_ucs2, seed=42), h)
