# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_duck_corogen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CoroGenLike:

        def send(self):
            pass

        def throw(self):
            pass

        def close(self):
            pass

        def __await__(self):
            return self

        def __iter__(self):
            return self

        def __next__(self):
            pass
    coro = CoroGenLike()

    @types.coroutine
    def foo():
        return coro
    self.assertIs(foo(), coro)
    self.assertIs(foo().__await__(), coro)
