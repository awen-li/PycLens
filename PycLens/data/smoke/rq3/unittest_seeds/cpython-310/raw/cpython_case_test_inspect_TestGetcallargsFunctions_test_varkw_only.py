# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetcallargsFunctions_test_varkw_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.makeCallable('**c')
    self.assertEqualCallArgs(f, '')
    self.assertEqualCallArgs(f, 'a=1')
    self.assertEqualCallArgs(f, 'a=1, b=2')
    self.assertEqualCallArgs(f, 'c=3, **{"a": 1, "b": 2}')
    self.assertEqualCallArgs(f, '**collections.UserDict(a=1, b=2)')
    self.assertEqualCallArgs(f, 'c=3, **collections.UserDict(a=1, b=2)')
