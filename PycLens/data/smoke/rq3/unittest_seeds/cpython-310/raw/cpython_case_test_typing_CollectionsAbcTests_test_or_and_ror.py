# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_or_and_ror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(typing.Sized | typing.Awaitable, Union[typing.Sized, typing.Awaitable])
    self.assertEqual(typing.Coroutine | typing.Hashable, Union[typing.Coroutine, typing.Hashable])
