# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_async_for

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Done(Exception):
        pass

    class AIter:

        def __aiter__(self):
            return self

        async def __anext__(self):
            raise StopAsyncIteration

    async def foo():
        async for i in AIter():
            pass
        async for (i, j) in AIter():
            pass
        async for i in AIter():
            pass
        else:
            pass
        raise Done
    with self.assertRaises(Done):
        foo().send(None)
