# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: CellTest_test_comparison

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(cell(2) < cell(3))
    self.assertTrue(empty_cell() < cell('saturday'))
    self.assertTrue(empty_cell() == empty_cell())
    self.assertTrue(cell(-36) == cell(-36.0))
    self.assertTrue(cell(True) > empty_cell())
