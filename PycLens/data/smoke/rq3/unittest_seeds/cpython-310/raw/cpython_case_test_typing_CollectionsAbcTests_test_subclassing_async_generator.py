# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_subclassing_async_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class G(typing.AsyncGenerator[int, int]):

        def asend(self, value):
            pass

        def athrow(self, typ, val=None, tb=None):
            pass
    ns = {}
    exec('async def g(): yield 0', globals(), ns)
    g = ns['g']
    self.assertIsSubclass(G, typing.AsyncGenerator)
    self.assertIsSubclass(G, typing.AsyncIterable)
    self.assertIsSubclass(G, collections.abc.AsyncGenerator)
    self.assertIsSubclass(G, collections.abc.AsyncIterable)
    self.assertNotIsSubclass(type(g), G)
    instance = G()
    self.assertIsInstance(instance, typing.AsyncGenerator)
    self.assertIsInstance(instance, typing.AsyncIterable)
    self.assertIsInstance(instance, collections.abc.AsyncGenerator)
    self.assertIsInstance(instance, collections.abc.AsyncIterable)
    self.assertNotIsInstance(type(g), G)
    self.assertNotIsInstance(g, G)
