# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_python_async_iterator_types_coroutine_anext

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import types

    class MyAsyncIterWithTypesCoro:
        """Asynchronously yield 1, then 2."""

        def __init__(self):
            self.yielded = 0

        def __aiter__(self):
            return self

        @types.coroutine
        def __anext__(self):
            if False:
                yield 'this is a generator-based coroutine'
            if self.yielded >= 2:
                raise StopAsyncIteration()
            else:
                self.yielded += 1
                return self.yielded
    self.check_async_iterator_anext(MyAsyncIterWithTypesCoro)
