# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: KDFTests_test_normalized_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertNotIn('blake2b512', hashlib.algorithms_available)
    self.assertNotIn('sha3-512', hashlib.algorithms_available)
