# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetcallargsFunctions_test_varkw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.makeCallable('a, b=1, **c')
    self.assertEqualCallArgs(f, 'a=2')
    self.assertEqualCallArgs(f, '2, b=3, c=4')
    self.assertEqualCallArgs(f, 'b=3, a=2, c=4')
    self.assertEqualCallArgs(f, 'c=4, **{"a":2, "b":3}')
    self.assertEqualCallArgs(f, '2, c=4, **{"b":3}')
    self.assertEqualCallArgs(f, 'b=2, **{"a":3, "c":4}')
    self.assertEqualCallArgs(f, '**collections.UserDict(a=2, b=3, c=4)')
    self.assertEqualCallArgs(f, '2, c=4, **collections.UserDict(b=3)')
    self.assertEqualCallArgs(f, 'b=2, **collections.UserDict(a=3, c=4)')
