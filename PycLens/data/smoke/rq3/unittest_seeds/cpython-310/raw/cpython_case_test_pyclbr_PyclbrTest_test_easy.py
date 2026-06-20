# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyclbr.py
# case: PyclbrTest_test_easy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkModule('pyclbr')
    self.checkModule('doctest', ignore=('TestResults', '_SpoofOut', 'DocTestCase', '_DocTestSuite'))
    self.checkModule('difflib', ignore=('Match',))
