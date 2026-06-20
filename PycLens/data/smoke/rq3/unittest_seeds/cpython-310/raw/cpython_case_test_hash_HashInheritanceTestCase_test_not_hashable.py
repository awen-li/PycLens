# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashInheritanceTestCase_test_not_hashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in self.error_expected:
        self.assertNotIsInstance(obj, Hashable)
