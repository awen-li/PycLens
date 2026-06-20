# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_AsyncGenerator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NonAGen1:

        def __aiter__(self):
            return self

        def __anext__(self):
            return None

        def aclose(self):
            pass

        def athrow(self, typ, val=None, tb=None):
            pass

    class NonAGen2:

        def __aiter__(self):
            return self

        def __anext__(self):
            return None

        def aclose(self):
            pass

        def asend(self, value):
            return value

    class NonAGen3:

        def aclose(self):
            pass

        def asend(self, value):
            return value

        def athrow(self, typ, val=None, tb=None):
            pass
    non_samples = [None, 42, 3.14, 1j, b'', '', (), [], {}, set(), iter(()), iter([]), NonAGen1(), NonAGen2(), NonAGen3()]
    for x in non_samples:
        self.assertNotIsInstance(x, AsyncGenerator)
        self.assertFalse(issubclass(type(x), AsyncGenerator), repr(type(x)))

    class Gen:

        def __aiter__(self):
            return self

        async def __anext__(self):
            return None

        async def aclose(self):
            pass

        async def asend(self, value):
            return value

        async def athrow(self, typ, val=None, tb=None):
            pass

    class MinimalAGen(AsyncGenerator):

        async def asend(self, value):
            return value

        async def athrow(self, typ, val=None, tb=None):
            await super().athrow(typ, val, tb)

    async def gen():
        yield 1
    samples = [gen(), Gen(), MinimalAGen()]
    for x in samples:
        self.assertIsInstance(x, AsyncIterator)
        self.assertIsInstance(x, AsyncGenerator)
        self.assertTrue(issubclass(type(x), AsyncGenerator), repr(type(x)))
    self.validate_abstract_methods(AsyncGenerator, 'asend', 'athrow')

    def run_async(coro):
        result = None
        while True:
            try:
                coro.send(None)
            except StopIteration as ex:
                result = ex.args[0] if ex.args else None
                break
        return result
    mgen = MinimalAGen()
    self.assertIs(mgen, mgen.__aiter__())
    self.assertIs(run_async(mgen.asend(None)), run_async(mgen.__anext__()))
    self.assertEqual(2, run_async(mgen.asend(2)))
    self.assertIsNone(run_async(mgen.aclose()))
    with self.assertRaises(ValueError):
        run_async(mgen.athrow(ValueError))

    class FailOnClose(AsyncGenerator):

        async def asend(self, value):
            return value

        async def athrow(self, *args):
            raise ValueError
    with self.assertRaises(ValueError):
        run_async(FailOnClose().aclose())

    class IgnoreGeneratorExit(AsyncGenerator):

        async def asend(self, value):
            return value

        async def athrow(self, *args):
            pass
    with self.assertRaises(RuntimeError):
        run_async(IgnoreGeneratorExit().aclose())
