# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_async_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = {}
    exec('async def f():\n    yield 42\n', globals(), ns)
    g = ns['f']()
    self.assertIsSubclass(type(g), typing.AsyncGenerator)
