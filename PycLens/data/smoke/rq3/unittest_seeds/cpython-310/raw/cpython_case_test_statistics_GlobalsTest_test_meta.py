# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: GlobalsTest_test_meta

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for meta in self.expected_metadata:
        self.assertTrue(hasattr(self.module, meta), '%s not present' % meta)
