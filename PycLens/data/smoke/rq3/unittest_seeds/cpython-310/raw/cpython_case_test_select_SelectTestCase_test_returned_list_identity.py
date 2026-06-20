# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_select.py
# case: SelectTestCase_test_returned_list_identity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w, x) = select.select([], [], [], 1)
    self.assertIsNot(r, w)
    self.assertIsNot(r, x)
    self.assertIsNot(w, x)
