# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_detect_api_mismatch__ignore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ignore = ['attribute1', 'attribute3', '__magic_2__', 'not_in_either']
    missing_items = support.detect_api_mismatch(self.RefClass, self.OtherClass, ignore=ignore)
    self.assertEqual(set(), missing_items)
    missing_items = support.detect_api_mismatch(self.OtherClass, self.RefClass, ignore=ignore)
    self.assertEqual(set(), missing_items)
