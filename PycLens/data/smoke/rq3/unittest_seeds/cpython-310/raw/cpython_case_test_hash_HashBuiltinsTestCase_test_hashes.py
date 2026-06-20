# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashBuiltinsTestCase_test_hashes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _default_hash = object.__hash__
    for obj in self.hashes_to_check:
        self.assertEqual(hash(obj), _default_hash(obj))
