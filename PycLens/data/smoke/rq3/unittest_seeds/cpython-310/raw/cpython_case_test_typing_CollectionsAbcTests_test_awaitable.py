# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_awaitable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = {}
    exec('async def foo() -> typing.Awaitable[int]:\n    return await AwaitableWrapper(42)\n', globals(), ns)
    foo = ns['foo']
    g = foo()
    self.assertIsInstance(g, typing.Awaitable)
    self.assertNotIsInstance(foo, typing.Awaitable)
    g.send(None)
