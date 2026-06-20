# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_AsyncIterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AI:

        def __aiter__(self):
            return self

        async def __anext__(self):
            raise StopAsyncIteration
    self.assertTrue(isinstance(AI(), AsyncIterator))
    self.assertTrue(issubclass(AI, AsyncIterator))
    non_samples = [None, object, []]
    for x in non_samples:
        self.assertNotIsInstance(x, AsyncIterator)
        self.assertFalse(issubclass(type(x), AsyncIterator), repr(type(x)))

    class AnextOnly:

        async def __anext__(self):
            raise StopAsyncIteration
    self.assertNotIsInstance(AnextOnly(), AsyncIterator)
    self.validate_abstract_methods(AsyncIterator, '__anext__', '__aiter__')
