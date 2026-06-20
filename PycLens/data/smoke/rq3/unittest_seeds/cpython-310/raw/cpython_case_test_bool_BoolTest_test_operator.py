# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_operator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import operator
    self.assertIs(operator.truth(0), False)
    self.assertIs(operator.truth(1), True)
    self.assertIs(operator.not_(1), False)
    self.assertIs(operator.not_(0), True)
    self.assertIs(operator.contains([], 1), False)
    self.assertIs(operator.contains([1], 1), True)
    self.assertIs(operator.lt(0, 0), False)
    self.assertIs(operator.lt(0, 1), True)
    self.assertIs(operator.is_(True, True), True)
    self.assertIs(operator.is_(True, False), False)
    self.assertIs(operator.is_not(True, True), False)
    self.assertIs(operator.is_not(True, False), True)
