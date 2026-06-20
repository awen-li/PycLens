# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeGuardTests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TypeGuard[int]

    def foo(arg) -> TypeGuard[int]:
        ...
    self.assertEqual(gth(foo), {'return': TypeGuard[int]})
