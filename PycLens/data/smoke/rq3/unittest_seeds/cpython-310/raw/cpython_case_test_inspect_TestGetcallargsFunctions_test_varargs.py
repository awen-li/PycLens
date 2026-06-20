# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetcallargsFunctions_test_varargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.makeCallable('a, b=1, *c')
    self.assertEqualCallArgs(f, '2')
    self.assertEqualCallArgs(f, '2, 3')
    self.assertEqualCallArgs(f, '2, 3, 4')
    self.assertEqualCallArgs(f, '*(2,3,4)')
    self.assertEqualCallArgs(f, '2, *[3,4]')
    self.assertEqualCallArgs(f, '2, 3, *collections.UserList([4])')
