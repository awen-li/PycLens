# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_detect_api_mismatch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    missing_items = support.detect_api_mismatch(self.RefClass, self.OtherClass)
    self.assertEqual({'attribute1'}, missing_items)
    missing_items = support.detect_api_mismatch(self.OtherClass, self.RefClass)
    self.assertEqual({'attribute3', '__magic_2__'}, missing_items)
