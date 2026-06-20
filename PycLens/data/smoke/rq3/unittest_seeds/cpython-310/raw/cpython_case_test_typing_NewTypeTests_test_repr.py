# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NewTypeTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(UserId), f'{__name__}.UserId')
    self.assertEqual(repr(self.UserName), f'{__name__}.{self.__class__.__qualname__}.UserName')
