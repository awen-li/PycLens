# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NewTypeTests_test_or

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for cls in (int, self.UserName):
        with self.subTest(cls=cls):
            self.assertEqual(UserId | cls, Union[UserId, cls])
            self.assertEqual(cls | UserId, Union[cls, UserId])
            self.assertEqual(get_args(UserId | cls), (UserId, cls))
            self.assertEqual(get_args(cls | UserId), (cls, UserId))
