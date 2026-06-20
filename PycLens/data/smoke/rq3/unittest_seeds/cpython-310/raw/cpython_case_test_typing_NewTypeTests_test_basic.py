# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NewTypeTests_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(UserId(5), int)
    self.assertIsInstance(self.UserName('Joe'), str)
    self.assertEqual(UserId(5) + 1, 6)
