# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: NumberTest_test_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkvalue('lt', 0, 0, False)
    self.checkvalue('le', 0, 0, True)
    self.checkvalue('eq', 0, 0, True)
    self.checkvalue('ne', 0, 0, False)
    self.checkvalue('gt', 0, 0, False)
    self.checkvalue('ge', 0, 0, True)
    self.checkvalue('lt', 0, 1, True)
    self.checkvalue('le', 0, 1, True)
    self.checkvalue('eq', 0, 1, False)
    self.checkvalue('ne', 0, 1, True)
    self.checkvalue('gt', 0, 1, False)
    self.checkvalue('ge', 0, 1, False)
    self.checkvalue('lt', 1, 0, False)
    self.checkvalue('le', 1, 0, False)
    self.checkvalue('eq', 1, 0, False)
    self.checkvalue('ne', 1, 0, True)
    self.checkvalue('gt', 1, 0, True)
    self.checkvalue('ge', 1, 0, True)
