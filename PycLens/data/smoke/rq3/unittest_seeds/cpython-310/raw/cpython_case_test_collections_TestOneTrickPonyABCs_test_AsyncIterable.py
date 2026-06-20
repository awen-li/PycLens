# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_AsyncIterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AI:

        def __aiter__(self):
            return self
    self.assertTrue(isinstance(AI(), AsyncIterable))
    self.assertTrue(issubclass(AI, AsyncIterable))
    non_samples = [None, object, []]
    for x in non_samples:
        self.assertNotIsInstance(x, AsyncIterable)
        self.assertFalse(issubclass(type(x), AsyncIterable), repr(type(x)))
    self.validate_abstract_methods(AsyncIterable, '__aiter__')
    self.validate_isinstance(AsyncIterable, '__aiter__')
