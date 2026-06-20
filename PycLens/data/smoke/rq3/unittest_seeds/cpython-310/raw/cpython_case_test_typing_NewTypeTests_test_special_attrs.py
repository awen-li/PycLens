# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NewTypeTests_test_special_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(UserId.__name__, 'UserId')
    self.assertEqual(UserId.__qualname__, 'UserId')
    self.assertEqual(UserId.__module__, __name__)
    self.assertEqual(UserId.__supertype__, int)
    UserName = self.UserName
    self.assertEqual(UserName.__name__, 'UserName')
    self.assertEqual(UserName.__qualname__, self.__class__.__qualname__ + '.UserName')
    self.assertEqual(UserName.__module__, __name__)
    self.assertEqual(UserName.__supertype__, str)
