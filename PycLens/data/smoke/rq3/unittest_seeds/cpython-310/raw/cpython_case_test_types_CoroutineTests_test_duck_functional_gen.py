# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_duck_functional_gen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Generator:
        """Emulates the following generator (very clumsy):

              def gen(fut):
                  result = yield fut
                  return result * 2
            """

        def __init__(self, fut):
            self._i = 0
            self._fut = fut

        def __iter__(self):
            return self

        def __next__(self):
            return self.send(None)

        def send(self, v):
            try:
                if self._i == 0:
                    assert v is None
                    return self._fut
                if self._i == 1:
                    raise StopIteration(v * 2)
                if self._i > 1:
                    raise StopIteration
            finally:
                self._i += 1

        def throw(self, tp, *exc):
            self._i = 100
            if tp is not GeneratorExit:
                raise tp

        def close(self):
            self.throw(GeneratorExit)

    @types.coroutine
    def foo():
        return Generator('spam')
    wrapper = foo()
    self.assertIsInstance(wrapper, types._GeneratorWrapper)

    async def corofunc():
        return await foo() + 100
    coro = corofunc()
    self.assertEqual(coro.send(None), 'spam')
    try:
        coro.send(20)
    except StopIteration as ex:
        self.assertEqual(ex.args[0], 140)
    else:
        self.fail('StopIteration was expected')
