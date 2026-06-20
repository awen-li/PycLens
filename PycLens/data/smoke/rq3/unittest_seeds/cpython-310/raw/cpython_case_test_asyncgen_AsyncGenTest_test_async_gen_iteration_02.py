# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenTest_test_async_gen_iteration_02

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        await awaitable()
        yield 123
        await awaitable()
    g = gen()
    ai = g.__aiter__()
    an = ai.__anext__()
    self.assertEqual(an.__next__(), ('result',))
    try:
        an.__next__()
    except StopIteration as ex:
        self.assertEqual(ex.args[0], 123)
    else:
        self.fail('StopIteration was not raised')
    an = ai.__anext__()
    self.assertEqual(an.__next__(), ('result',))
    try:
        an.__next__()
    except StopAsyncIteration as ex:
        self.assertFalse(ex.args)
    else:
        self.fail('StopAsyncIteration was not raised')
