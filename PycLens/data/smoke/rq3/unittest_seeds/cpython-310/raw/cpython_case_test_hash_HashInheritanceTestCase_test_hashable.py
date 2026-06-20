# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashInheritanceTestCase_test_hashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    objects = self.default_expected + self.fixed_expected
    for obj in objects:
        self.assertIsInstance(obj, Hashable)
