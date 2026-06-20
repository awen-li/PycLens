# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetcallargsFunctions_test_multiple_features

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.makeCallable('a, b=2, *f, **g')
    self.assertEqualCallArgs(f, '2, 3, 7')
    self.assertEqualCallArgs(f, '2, 3, x=8')
    self.assertEqualCallArgs(f, '2, 3, x=8, *[(4,[5,6]), 7]')
    self.assertEqualCallArgs(f, '2, x=8, *[3, (4,[5,6]), 7], y=9')
    self.assertEqualCallArgs(f, 'x=8, *[2, 3, (4,[5,6])], y=9')
    self.assertEqualCallArgs(f, 'x=8, *collections.UserList([2, 3, (4,[5,6])]), **{"y":9, "z":10}')
    self.assertEqualCallArgs(f, '2, x=8, *collections.UserList([3, (4,[5,6])]), **collections.UserDict(y=9, z=10)')
    f = self.makeCallable('a, b=2, *f, x, y=99, **g')
    self.assertEqualCallArgs(f, '2, 3, x=8')
    self.assertEqualCallArgs(f, '2, 3, x=8, *[(4,[5,6]), 7]')
    self.assertEqualCallArgs(f, '2, x=8, *[3, (4,[5,6]), 7], y=9, z=10')
    self.assertEqualCallArgs(f, 'x=8, *[2, 3, (4,[5,6])], y=9, z=10')
    self.assertEqualCallArgs(f, 'x=8, *collections.UserList([2, 3, (4,[5,6])]), q=0, **{"y":9, "z":10}')
    self.assertEqualCallArgs(f, '2, x=8, *collections.UserList([3, (4,[5,6])]), q=0, **collections.UserDict(y=9, z=10)')
