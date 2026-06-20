# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetcallargsFunctions_test_keyword_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.makeCallable('a=3, *, c, d=2')
    self.assertEqualCallArgs(f, 'c=3')
    self.assertEqualCallArgs(f, 'c=3, a=3')
    self.assertEqualCallArgs(f, 'a=2, c=4')
    self.assertEqualCallArgs(f, '4, c=4')
    self.assertEqualException(f, '')
    self.assertEqualException(f, '3')
    self.assertEqualException(f, 'a=3')
    self.assertEqualException(f, 'd=4')
    f = self.makeCallable('*, c, d=2')
    self.assertEqualCallArgs(f, 'c=3')
    self.assertEqualCallArgs(f, 'c=3, d=4')
    self.assertEqualCallArgs(f, 'd=4, c=3')
