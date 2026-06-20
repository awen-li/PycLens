# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashInheritanceTestCase_test_default_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in self.default_expected:
        self.assertEqual(hash(obj), _default_hash(obj))
